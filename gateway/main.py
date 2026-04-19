"""
Gateway Service
───────────────
• Accepts browser WebSocket connections
• Broadcasts committed strokes to all clients
• (Phase 2) Will forward strokes → current leader replica
• (Phase 2) Will auto-reroute on leader failover
"""

import asyncio
import json
import logging
import os

import httpx
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [GATEWAY] %(levelname)s %(message)s",
)
log = logging.getLogger(__name__)

app = FastAPI(title="Drawing-Board Gateway")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Serve frontend statically ─────────────────────────────────
FRONTEND_DIR = os.path.join(os.path.dirname(__file__), "..", "frontend")
if os.path.isdir(FRONTEND_DIR):
    app.mount("/app", StaticFiles(directory=FRONTEND_DIR, html=True), name="frontend")

# ── Replica addresses (used in Phase 2) ──────────────────────
REPLICAS = {
    "replica1": os.getenv("REPLICA1_URL", "http://replica1:8001"),
    "replica2": os.getenv("REPLICA2_URL", "http://replica2:8002"),
    "replica3": os.getenv("REPLICA3_URL", "http://replica3:8003"),
}

# ── In-memory state ───────────────────────────────────────────
connected_clients: list[WebSocket] = []
stroke_log: list[dict] = []          # committed strokes (replayed to new joiners)
current_leader: str | None = None    # set once replicas are running


# ═════════════════════════════════════════════════════════════
# Helper: broadcast a message to every connected browser client
# ═════════════════════════════════════════════════════════════
async def broadcast(payload: dict, exclude: WebSocket | None = None):
    dead = []
    for ws in connected_clients:
        if ws is exclude:
            continue
        try:
            await ws.send_text(json.dumps(payload))
        except Exception:
            dead.append(ws)
    for ws in dead:
        connected_clients.remove(ws)


# ═════════════════════════════════════════════════════════════
# Helper: find which replica is currently leader
# ═════════════════════════════════════════════════════════════
async def discover_leader() -> str | None:
    """Poll all replicas and return the id of the one claiming leadership."""
    async with httpx.AsyncClient(timeout=1.0) as client:
        for name, url in REPLICAS.items():
            try:
                r = await client.get(f"{url}/status")
                if r.status_code == 200:
                    data = r.json()
                    if data.get("role") == "leader":
                        return name
            except Exception:
                pass
    return None


# ═════════════════════════════════════════════════════════════
# Helper: forward a stroke to the leader replica
# ═════════════════════════════════════════════════════════════
async def forward_to_leader(payload: dict) -> bool:
    """
    Send the stroke to the current leader via HTTP POST /stroke.
    Returns True if accepted, False if we need to find a new leader.
    """
    global current_leader
    if current_leader is None:
        current_leader = await discover_leader()
    if current_leader is None:
        log.warning("No leader found — broadcasting directly (degraded mode)")
        return False

    url = REPLICAS[current_leader]
    try:
        async with httpx.AsyncClient(timeout=2.0) as client:
            r = await client.post(f"{url}/stroke", json=payload)
            if r.status_code == 200:
                return True
            if r.status_code == 307:          # replica says "I'm not leader"
                redirect = r.json().get("leader")
                if redirect and redirect in REPLICAS:
                    current_leader = redirect
                    log.info(f"Redirected to leader: {redirect}")
                    return await forward_to_leader(payload)
    except Exception as e:
        log.warning(f"Leader {current_leader} unreachable: {e}")
        current_leader = None
    return False


# ═════════════════════════════════════════════════════════════
# REST endpoint: replicas call this to push committed strokes
# ═════════════════════════════════════════════════════════════
@app.post("/commit")
async def receive_commit(payload: dict):
    """
    Called by the leader after a stroke reaches majority quorum.
    Gateway records it and fans out to all browsers.
    """
    stroke_log.append(payload)
    await broadcast({"type": "stroke", **payload})
    log.info(f"Committed stroke #{len(stroke_log)}")
    return {"ok": True}


# ═════════════════════════════════════════════════════════════
# REST endpoint: replicas call this to update the known leader
# ═════════════════════════════════════════════════════════════
@app.post("/leader")
async def update_leader(payload: dict):
    """Replicas post here when a new leader is elected."""
    global current_leader
    current_leader = payload.get("leader")
    log.info(f"Leader updated → {current_leader}")
    await broadcast({"type": "leader_info", "leader": current_leader})
    return {"ok": True}


# ═════════════════════════════════════════════════════════════
# REST endpoint: health / debug
# ═════════════════════════════════════════════════════════════
@app.get("/status")
async def status():
    return {
        "clients":        len(connected_clients),
        "leader":         current_leader,
        "committed":      len(stroke_log),
        "replicas":       list(REPLICAS.keys()),
    }


# ═════════════════════════════════════════════════════════════
# WebSocket endpoint: browser clients
# ═════════════════════════════════════════════════════════════
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connected_clients.append(websocket)
    client_addr = websocket.client
    log.info(f"Client connected: {client_addr}  (total={len(connected_clients)})")

    # Replay committed log so new joiners see existing canvas
    for stroke in stroke_log:
        try:
            await websocket.send_text(json.dumps({"type": "stroke", **stroke}))
        except Exception:
            break

    # Send current leader info
    if current_leader:
        await websocket.send_text(
            json.dumps({"type": "leader_info", "leader": current_leader})
        )

    try:
        while True:
            raw = await websocket.receive_text()
            msg = json.loads(raw)

            # ── Clear command ──────────────────────────────────
            if msg.get("type") == "clear":
                stroke_log.clear()
                await broadcast({"type": "clear"}, exclude=websocket)
                log.info("Canvas cleared")
                continue

            # ── Stroke ────────────────────────────────────────
            if msg.get("type") == "stroke":
                # Phase 1: replicas not yet running → broadcast directly
                # Phase 2: forward to leader replica for RAFT commit
                replicas_up = current_leader is not None
                if replicas_up:
                    ok = await forward_to_leader(msg)
                    if not ok:
                        # degraded: broadcast so canvas still works
                        stroke_log.append(msg)
                        await broadcast({"type": "stroke", **msg}, exclude=websocket)
                else:
                    # Direct broadcast (no replicas yet)
                    stroke_log.append(msg)
                    await broadcast({"type": "stroke", **msg}, exclude=websocket)

    except WebSocketDisconnect:
        log.info(f"Client disconnected: {client_addr}")
    except Exception as e:
        log.warning(f"Client error {client_addr}: {e}")
    finally:
        if websocket in connected_clients:
            connected_clients.remove(websocket)
        log.info(f"Remaining clients: {len(connected_clients)}")
