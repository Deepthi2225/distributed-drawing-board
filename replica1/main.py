"""
Replica Node — Mini-RAFT
─────────────────────────
Implements:
  • Follower / Candidate / Leader state machine
  • Randomised election timeouts (500–800 ms)
  • RequestVote RPC
  • AppendEntries / Heartbeat RPC
  • Log replication with majority commit
  • Catch-up sync for restarted nodes  (/sync-log)
  • Notifies gateway on commit + leader change
"""

import asyncio
import logging
import os
import random
import time

import httpx
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# ── Configuration ──────────────────────────────────────────────
REPLICA_ID   = os.getenv("REPLICA_ID",   "replica1")
PORT         = int(os.getenv("PORT",     "8001"))
GATEWAY_URL  = os.getenv("GATEWAY_URL",  "http://gateway:8000")

# Peer addresses come from env so docker-compose can wire them
PEERS: dict[str, str] = {}
for key, val in os.environ.items():
    if key.startswith("PEER_"):
        peer_id = key[5:].lower()          # PEER_REPLICA2 → replica2
        PEERS[peer_id] = val

# ── Timing constants ───────────────────────────────────────────
HEARTBEAT_INTERVAL   = 0.150   # seconds
ELECTION_TIMEOUT_MIN = 0.500
ELECTION_TIMEOUT_MAX = 0.800

logging.basicConfig(
    level=logging.INFO,
    format=f"%(asctime)s [{REPLICA_ID.upper()}] %(levelname)s %(message)s",
)
log = logging.getLogger(__name__)

# ══════════════════════════════════════════════════════════════
# RAFT State
# ══════════════════════════════════════════════════════════════
class RaftState:
    def __init__(self):
        self.role         = "follower"
        self.term         = 0
        self.voted_for: str | None = None
        self.vote_granted_by: set[str] = set()

        self.log:          list[dict] = []
        self.commit_index: int        = -1

        self.leader_id:    str | None = None
        self.last_heartbeat: float    = time.time()

    @property
    def last_log_index(self) -> int:
        return len(self.log) - 1

    @property
    def last_log_term(self) -> int:
        return self.log[-1]["term"] if self.log else 0


raft = RaftState()

# ══════════════════════════════════════════════════════════════
# FastAPI app
# ══════════════════════════════════════════════════════════════
app = FastAPI(title=f"Replica {REPLICA_ID}")
app.add_middleware(CORSMiddleware, allow_origins=["*"],
                   allow_methods=["*"], allow_headers=["*"])


# ══════════════════════════════════════════════════════════════
# Utility: HTTP helpers
# ══════════════════════════════════════════════════════════════
async def post(url: str, data: dict, timeout: float = 1.0) -> dict | None:
    try:
        async with httpx.AsyncClient(timeout=timeout) as client:
            r = await client.post(url, json=data)
            return r.json() if r.status_code == 200 else None
    except Exception:
        return None


async def get(url: str, timeout: float = 1.0) -> dict | None:
    try:
        async with httpx.AsyncClient(timeout=timeout) as client:
            r = await client.get(url)
            return r.json() if r.status_code == 200 else None
    except Exception:
        return None


# ══════════════════════════════════════════════════════════════
# Notify gateway
# ══════════════════════════════════════════════════════════════
async def announce_leadership():
    await post(f"{GATEWAY_URL}/leader", {"leader": REPLICA_ID})
    log.info(f"Announced leadership to gateway (term={raft.term})")


async def push_commit_to_gateway(entry: dict):
    await post(f"{GATEWAY_URL}/commit", entry)


# ══════════════════════════════════════════════════════════════
# Catch-up sync — fetch missing entries from leader
# ══════════════════════════════════════════════════════════════
async def catch_up_with_leader():
    """
    Called when a follower is behind the leader.
    Tries all peers to find the leader and fetches missing entries.
    """
    await asyncio.sleep(0.2)  # small delay to let leader stabilize

    # Find leader URL
    leader_url = PEERS.get(raft.leader_id)

    if not leader_url:
        # Search all peers for the current leader
        for peer_id, peer_url in PEERS.items():
            result = await get(f"{peer_url}/status")
            if result and result.get("role") == "leader":
                leader_url = peer_url
                raft.leader_id = peer_id
                log.info(f"Found leader at {peer_id}")
                break

    if not leader_url:
        log.warning("Catch-up failed — no leader found")
        return

    from_index = len(raft.log)
    result = await get(f"{leader_url}/sync-log?from_index={from_index}")
    if not result:
        log.warning("Catch-up failed — sync-log request failed")
        return

    entries = result.get("entries", [])
    if entries:
        for entry in entries:
            idx = entry.get("index", len(raft.log))
            if idx >= len(raft.log):
                raft.log.append(entry)
        raft.commit_index = result.get("commit_index", raft.commit_index)
        log.info(
            f"Caught up: applied {len(entries)} entries — "
            f"log_length={len(raft.log)}, commit_index={raft.commit_index}"
        )
    else:
        log.info("Catch-up: already up to date")


# ══════════════════════════════════════════════════════════════
# RPC: /request-vote
# ══════════════════════════════════════════════════════════════
@app.post("/request-vote")
async def request_vote(payload: dict):
    candidate_term = payload["term"]
    candidate_id   = payload["candidate_id"]

    if candidate_term > raft.term:
        raft.term      = candidate_term
        raft.role      = "follower"
        raft.voted_for = None

    if candidate_term < raft.term:
        return {"term": raft.term, "vote_granted": False}

    already_voted = raft.voted_for not in (None, candidate_id)

    candidate_last_term  = payload.get("last_log_term",  0)
    candidate_last_index = payload.get("last_log_index", -1)
    log_ok = (
        candidate_last_term > raft.last_log_term or
        (candidate_last_term == raft.last_log_term and
         candidate_last_index >= raft.last_log_index)
    )

    if already_voted or not log_ok:
        return {"term": raft.term, "vote_granted": False}

    raft.voted_for      = candidate_id
    raft.last_heartbeat = time.time()
    log.info(f"Voted for {candidate_id} in term {raft.term}")
    return {"term": raft.term, "vote_granted": True}


# ══════════════════════════════════════════════════════════════
# RPC: /append-entries
# ══════════════════════════════════════════════════════════════
@app.post("/append-entries")
async def append_entries(payload: dict):
    leader_term = payload["term"]
    leader_id   = payload["leader_id"]

    if leader_term < raft.term:
        return {"term": raft.term, "success": False, "log_length": len(raft.log)}

    # Valid leader — reset state
    raft.term           = leader_term
    raft.role           = "follower"
    raft.leader_id      = leader_id
    raft.last_heartbeat = time.time()

    prev_index = payload.get("prev_log_index", -1)
    prev_term  = payload.get("prev_log_term",  0)

    # Consistency check
    if prev_index >= 0:
        if len(raft.log) <= prev_index or raft.log[prev_index]["term"] != prev_term:
            # We are behind — trigger catch-up
            asyncio.create_task(catch_up_with_leader())
            return {"term": raft.term, "success": False, "log_length": len(raft.log)}

    entry = payload.get("entry")
    if entry is not None:
        next_index = prev_index + 1
        if len(raft.log) > next_index:
            raft.log = raft.log[:next_index]
        raft.log.append(entry)

    # Advance commit index
    leader_commit = payload.get("leader_commit", -1)
    if leader_commit > raft.commit_index:
        raft.commit_index = min(leader_commit, len(raft.log) - 1)

    # If still behind leader, trigger catch-up
    if leader_commit > len(raft.log) - 1:
        asyncio.create_task(catch_up_with_leader())

    return {"term": raft.term, "success": True, "log_length": len(raft.log)}


# ══════════════════════════════════════════════════════════════
# RPC: /heartbeat
# ══════════════════════════════════════════════════════════════
@app.post("/heartbeat")
async def heartbeat(payload: dict):
    return await append_entries({**payload, "entry": None})


# ══════════════════════════════════════════════════════════════
# RPC: /sync-log
# ══════════════════════════════════════════════════════════════
@app.get("/sync-log")
async def sync_log(from_index: int = 0):
    """Leader serves missing committed entries to a lagging follower."""
    committed = raft.log[: raft.commit_index + 1]
    missing   = committed[from_index:]
    return {
        "entries":      missing,
        "commit_index": raft.commit_index,
        "term":         raft.term,
        "leader":       raft.leader_id or REPLICA_ID,
    }


@app.post("/sync-log")
async def apply_sync(payload: dict):
    """Follower receives pushed entries from leader."""
    entries      = payload.get("entries", [])
    commit_index = payload.get("commit_index", -1)

    for entry in entries:
        idx = entry.get("index", len(raft.log))
        if idx >= len(raft.log):
            raft.log.append(entry)

    if commit_index > raft.commit_index:
        raft.commit_index = min(commit_index, len(raft.log) - 1)

    log.info(f"Sync-log applied: {len(entries)} entries, commit_index={raft.commit_index}")
    return {"ok": True, "log_length": len(raft.log)}


# ══════════════════════════════════════════════════════════════
# REST: /stroke
# ══════════════════════════════════════════════════════════════
@app.post("/stroke")
async def receive_stroke(payload: dict):
    if raft.role != "leader":
        return {"error": "not leader", "leader": raft.leader_id}, 307

    entry = {
        "index": len(raft.log),
        "term":  raft.term,
        **payload,
    }
    raft.log.append(entry)
    log.info(f"New stroke at index {entry['index']}")
    asyncio.create_task(replicate_entry(entry))
    return {"ok": True, "index": entry["index"]}


# ══════════════════════════════════════════════════════════════
# REST: /status
# ══════════════════════════════════════════════════════════════
@app.get("/status")
async def status():
    return {
        "id":           REPLICA_ID,
        "role":         raft.role,
        "term":         raft.term,
        "leader":       raft.leader_id,
        "log_length":   len(raft.log),
        "commit_index": raft.commit_index,
        "peers":        list(PEERS.keys()),
    }


# ══════════════════════════════════════════════════════════════
# Core RAFT background tasks
# ══════════════════════════════════════════════════════════════
async def replicate_entry(entry: dict):
    """Send AppendEntries to all peers; commit when majority ACK."""
    acks     = 1
    majority = (len(PEERS) + 1) // 2 + 1

    prev_index = entry["index"] - 1
    prev_term  = raft.log[prev_index]["term"] if prev_index >= 0 else 0

    tasks = []
    for peer_id, peer_url in PEERS.items():
        tasks.append(
            post(f"{peer_url}/append-entries", {
                "term":           raft.term,
                "leader_id":      REPLICA_ID,
                "prev_log_index": prev_index,
                "prev_log_term":  prev_term,
                "entry":          entry,
                "leader_commit":  raft.commit_index,
            })
        )

    results = await asyncio.gather(*tasks)

    for peer_id, result in zip(PEERS.keys(), results):
        if result and result.get("success"):
            acks += 1
        elif result and result.get("term", 0) > raft.term:
            raft.term = result["term"]
            raft.role = "follower"
            log.warning("Stepping down — saw higher term from peer")
            return

    if acks >= majority and entry["index"] > raft.commit_index:
        raft.commit_index = entry["index"]
        log.info(f"Committed entry {entry['index']} (acks={acks}/{len(PEERS)+1})")
        await push_commit_to_gateway(entry)


async def send_heartbeats():
    """Leader sends periodic heartbeats to all followers."""
    tasks = []
    for peer_id, peer_url in PEERS.items():
        tasks.append(
            post(f"{peer_url}/heartbeat", {
                "term":           raft.term,
                "leader_id":      REPLICA_ID,
                "prev_log_index": raft.last_log_index,
                "prev_log_term":  raft.last_log_term,
                "leader_commit":  raft.commit_index,
            })
        )
    results = await asyncio.gather(*tasks, return_exceptions=True)

    for result in results:
        if isinstance(result, dict) and result.get("term", 0) > raft.term:
            raft.term = result["term"]
            raft.role = "follower"
            log.warning("Stepping down during heartbeat — higher term seen")
            return


async def start_election():
    raft.role            = "candidate"
    raft.term           += 1
    raft.voted_for       = REPLICA_ID
    raft.vote_granted_by = {REPLICA_ID}
    log.info(f"Starting election for term {raft.term}")

    majority = (len(PEERS) + 1) // 2 + 1

    tasks = []
    for peer_id, peer_url in PEERS.items():
        tasks.append(
            post(f"{peer_url}/request-vote", {
                "term":           raft.term,
                "candidate_id":   REPLICA_ID,
                "last_log_index": raft.last_log_index,
                "last_log_term":  raft.last_log_term,
            })
        )

    results = await asyncio.gather(*tasks, return_exceptions=True)

    for peer_id, result in zip(PEERS.keys(), results):
        if isinstance(result, dict):
            if result.get("term", 0) > raft.term:
                raft.term      = result["term"]
                raft.role      = "follower"
                raft.voted_for = None
                log.info("Reverted to follower — higher term in vote response")
                return
            if result.get("vote_granted"):
                raft.vote_granted_by.add(peer_id)

    if len(raft.vote_granted_by) >= majority and raft.role == "candidate":
        raft.role      = "leader"
        raft.leader_id = REPLICA_ID
        log.info(f"🏆  Became LEADER for term {raft.term}")
        await announce_leadership()
        await send_heartbeats()
    else:
        log.info(f"Election failed — votes={len(raft.vote_granted_by)}/{len(PEERS)+1}")
        raft.role = "follower"


async def raft_loop():
    await asyncio.sleep(1.0)   # startup grace period

    while True:
        if raft.role == "leader":
            await send_heartbeats()
            await asyncio.sleep(HEARTBEAT_INTERVAL)

        elif raft.role in ("follower", "candidate"):
            timeout = random.uniform(ELECTION_TIMEOUT_MIN, ELECTION_TIMEOUT_MAX)
            await asyncio.sleep(timeout)

            elapsed = time.time() - raft.last_heartbeat
            if elapsed >= timeout and raft.role != "leader":
                await start_election()


@app.on_event("startup")
async def startup():
    log.info(f"Starting replica {REPLICA_ID}  peers={list(PEERS.keys())}")
    asyncio.create_task(raft_loop())
    # Trigger catch-up on startup in case we are rejoining the cluster
    asyncio.create_task(catch_up_with_leader())
