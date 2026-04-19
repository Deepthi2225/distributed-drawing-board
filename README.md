# Distributed Drawing Board with Mini-RAFT

A real-time collaborative drawing board built with FastAPI, WebSockets, and a 3-node RAFT-style replica cluster.

## What This Project Does

- Serves a browser drawing board UI.
- Accepts drawing strokes over WebSocket through a gateway.
- Replicates strokes through a mini-RAFT cluster (leader + followers).
- Commits strokes after majority acknowledgment.
- Broadcasts committed strokes to connected clients.
- Handles leader changes and follower catch-up.

## Project Structure

- `gateway/main.py`: WebSocket gateway, frontend static hosting, leader discovery, commit fan-out.
- `replica1/main.py`, `replica2/main.py`, `replica3/main.py`: Replica services running RAFT logic.
- `frontend/index.html`, `frontend/canvas.js`: Browser UI and drawing client logic.
- `docker-compose.yml`: Orchestrates gateway + 3 replicas.
- `Dockerfile.gateway`, `Dockerfile.replica`: Runtime images.
- `requirements.txt`: Python dependencies.

## Architecture Overview

1. Browser connects to gateway on `ws://localhost:8000/ws`.
2. Browser sends stroke messages to gateway.
3. Gateway forwards strokes to current leader (`POST /stroke`).
4. Leader appends log entry and replicates via `POST /append-entries`.
5. After quorum, leader commits and notifies gateway (`POST /commit`).
6. Gateway broadcasts committed stroke to all clients.

Gateway also listens for leader updates from replicas via `POST /leader`.

## Prerequisites

- Docker Desktop (or Docker Engine) installed and running.
- Docker Compose v2 (`docker compose`) available.
- A modern browser.

## Quick Start

From the project root:

```powershell
docker compose up -d --build
```

Open the app:

- `http://localhost:8000/app`

Check service status:

- Gateway: `http://localhost:8000/status`
- Replica 1: `http://localhost:8001/status`
- Replica 2: `http://localhost:8002/status`
- Replica 3: `http://localhost:8003/status`

To stop:

```powershell
docker compose down
```

To stop and remove volumes/networks/images created by compose:

```powershell
docker compose down --volumes --rmi local
```

## Expected Behavior

- Canvas loads from gateway static route (`/app`).
- WebSocket status in UI changes to Connected.
- Leader field updates when a leader is elected.
- Drawing in one browser tab appears in other connected tabs.
- Clearing canvas in one tab clears others.

## Failover Demo

1. Start stack with `docker compose up -d --build`.
2. Open 2 browser tabs at `http://localhost:8000/app`.
3. Draw a few strokes.
4. Identify current leader from UI or `GET /status` on replicas.
5. Stop the leader container, for example:
   - `docker stop replica2`
6. Wait briefly for election.
7. Continue drawing; cluster should resume with new leader.
8. Restart old leader:
   - `docker start replica2`
9. Replica should rejoin and catch up.

## Scenario Evidence (Live Run)

Full detailed outputs are captured in `scenario_report_clean.md`.

Screenshot files:

- `screenshots/case1.png`
- `screenshots/case2.png`
- `screenshots/case3.png`
- `screenshots/case4.png`
- `screenshots/case5.png`
- `screenshots/case6.png`

### Case 1 - Multiple tabs/users drawing

- Gateway reported active clients: 5
- Leader present during run: replica3

### Case 2 - Killing leader

- Leader container stop action succeeded (`docker stop replica3`)
- Cluster continued and elected/served through a new leader path

### Case 3 - Automatic failover

- Gateway status remained healthy after failover
- Replica statuses showed stable leader/follower roles after election

### Case 4 - Hot-reload replica after file edit

- Replica log showed file-watch trigger and reload sequence:
  - "WatchFiles detected changes in 'replica/main.py'. Reloading..."
  - "Shutting down" -> "Started server process" -> "Application startup complete"

### Case 5 - Consistent state after restart

- Stroke posts accepted from index 0 through 7
- After follower restart, all replicas converged to:
  - `log_length: 8`
  - `commit_index: 7`

### Case 6 - Chaotic/stress behavior

- Rapid stop/start operations completed
- Final cluster status recovered to healthy
- Final replicas remained consistent (`log_length: 8`, `commit_index: 7`)

## API/Protocol Notes

### Gateway Endpoints

- `GET /status`: gateway health and state.
- `POST /commit`: replicas push committed entries.
- `POST /leader`: replicas announce new leader.
- `WS /ws`: browser realtime channel.

### Replica Endpoints

- `GET /status`: replica role/term/log state.
- `POST /stroke`: leader accepts client stroke entries.
- `POST /request-vote`: election RPC.
- `POST /append-entries`: replication RPC.
- `POST /heartbeat`: heartbeat RPC.
- `GET /sync-log`: follower catch-up pull.
- `POST /sync-log`: follower catch-up apply.

## Verification Done in This Review

- Source-level checks completed for gateway, replicas, and frontend.
- No editor-reported errors in:
  - `gateway/main.py`
  - `replica1/main.py`
  - `replica2/main.py`
  - `replica3/main.py`
  - `frontend/canvas.js`
  - `frontend/index.html`
- Historical logs (`logs_failover_demo.txt`, `failover_logs.txt`) show successful:
  - service startup,
  - WebSocket connections,
  - leader announcements,
  - heartbeat traffic,
  - replica restarts and rejoin behavior.

Note: Live runtime verification was initially blocked while Docker engine was down, then completed successfully after Docker was started.

## Troubleshooting

### Docker Engine Not Running

If you see errors like:

- `open //./pipe/dockerDesktopLinuxEngine: The system cannot find the file specified`

Start Docker Desktop, wait until it reports engine running, then retry:

```powershell
docker compose up -d --build
```

### Compose Warning About `version`

Compose may warn that `version` is obsolete. This is non-blocking for Compose v2. You can remove the top-level `version` key from `docker-compose.yml` to silence the warning.

### WebSocket Not Connecting

- Ensure gateway container is up and mapped to port `8000`.
- Verify browser is opened at `http://localhost:8000/app`.
- Check gateway logs:

```powershell
docker compose logs -f gateway
```

### No Leader in UI

- Check replica statuses (`/status`) on ports `8001..8003`.
- Confirm all replicas are running:

```powershell
docker compose ps
```

- Inspect replica logs:

```powershell
docker compose logs -f replica1 replica2 replica3
```

## Useful Commands

```powershell
# View running services
docker compose ps

# Follow all logs
docker compose logs -f

# Rebuild and restart
docker compose up -d --build

# Stop everything
docker compose down
```
