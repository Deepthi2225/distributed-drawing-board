const canvas = document.getElementById("board");
const ctx = canvas.getContext("2d");

// ── UI elements ──────────────────────────────────────────────
const connStatus  = document.getElementById("conn-status");
const leaderEl    = document.getElementById("leader-id");
const strokeEl    = document.getElementById("stroke-count");
const colorPicker = document.getElementById("colorPicker");
const brushSize   = document.getElementById("brushSize");
const logEl       = document.getElementById("log");

// ── State ─────────────────────────────────────────────────────
let drawing     = false;
let lastX       = null;
let lastY       = null;
let strokeCount = 0;
let socket      = null;

// Unique ID for this tab so we can ignore our own echoes from gateway
const MY_ID = Math.random().toString(36).slice(2);

// ── Logging ───────────────────────────────────────────────────
function log(msg) {
    const line = document.createElement("div");
    line.textContent = `[${new Date().toLocaleTimeString()}] ${msg}`;
    logEl.prepend(line);
    if (logEl.children.length > 50) logEl.lastChild.remove();
}

// ── WebSocket setup ───────────────────────────────────────────
function connect() {
    const wsProtocol = window.location.protocol === "https:" ? "wss:" : "ws:";
    const wsUrl = `${wsProtocol}//${window.location.host}/ws`;
    socket = new WebSocket(wsUrl);

    socket.onopen = () => {
        connStatus.textContent = "Connected";
        connStatus.classList.add("connected");
        log("✅ Connected to gateway");
    };

    socket.onclose = () => {
        connStatus.textContent = "Disconnected";
        connStatus.classList.remove("connected");
        log("❌ Disconnected — retrying in 2s…");
        setTimeout(connect, 2000);
    };

    socket.onerror = () => {
        log("⚠️  WebSocket error");
    };

    socket.onmessage = (event) => {
        const msg = JSON.parse(event.data);

        // Leader info from gateway
        if (msg.type === "leader_info") {
            leaderEl.textContent = msg.leader || "none";
            log("👑 Leader is now: " + (msg.leader || "none"));
            return;
        }

        // Clear from another user
        if (msg.type === "clear") {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            strokeCount = 0;
            strokeEl.textContent = 0;
            log("🗑 Canvas cleared by another user");
            return;
        }

        // Stroke from another user — ignore our own echoes
        if (msg.type === "stroke") {
            if (msg.sender === MY_ID) return;
            drawSegment(msg);
            strokeCount++;
            strokeEl.textContent = strokeCount;
        }
    };
}

connect();

// ── Drawing helpers ───────────────────────────────────────────
function drawSegment(data) {
    ctx.beginPath();
    ctx.strokeStyle = data.color || "#000000";
    ctx.lineWidth   = data.size  || 3;
    ctx.lineCap     = "round";
    ctx.lineJoin    = "round";

    if (data.x0 != null && data.y0 != null) {
        ctx.moveTo(data.x0, data.y0);
        ctx.lineTo(data.x1, data.y1);
    } else {
        ctx.arc(data.x1, data.y1, (data.size || 3) / 2, 0, Math.PI * 2);
        ctx.fillStyle = data.color || "#000000";
        ctx.fill();
    }
    ctx.stroke();
}

function sendStroke(x0, y0, x1, y1) {
    if (!socket || socket.readyState !== WebSocket.OPEN) return;

    const payload = {
        type:   "stroke",
        sender: MY_ID,
        x0, y0, x1, y1,
        color:  colorPicker.value,
        size:   parseInt(brushSize.value),
    };

    socket.send(JSON.stringify(payload));

    // Count our own strokes immediately without waiting for echo
    strokeCount++;
    strokeEl.textContent = strokeCount;
}

// ── Mouse events ──────────────────────────────────────────────
canvas.addEventListener("mousedown", (e) => {
    drawing = true;
    const { x, y } = pos(e);
    lastX = x;
    lastY = y;

    // Draw dot locally immediately
    drawSegment({ x1: x, y1: y, color: colorPicker.value, size: parseInt(brushSize.value) });
    sendStroke(null, null, x, y);
});

canvas.addEventListener("mouseup", () => {
    drawing = false;
    lastX = null;
    lastY = null;
});

canvas.addEventListener("mouseleave", () => {
    drawing = false;
    lastX = null;
    lastY = null;
});

canvas.addEventListener("mousemove", (e) => {
    if (!drawing) return;
    const { x, y } = pos(e);

    // Draw locally immediately so it feels instant
    drawSegment({ x0: lastX, y0: lastY, x1: x, y1: y, color: colorPicker.value, size: parseInt(brushSize.value) });

    // Send to gateway for other users
    sendStroke(lastX, lastY, x, y);
    lastX = x;
    lastY = y;
});

// ── Touch support ─────────────────────────────────────────────
canvas.addEventListener("touchstart", (e) => {
    e.preventDefault();
    drawing = true;
    const { x, y } = pos(e.touches[0]);
    lastX = x;
    lastY = y;
    drawSegment({ x1: x, y1: y, color: colorPicker.value, size: parseInt(brushSize.value) });
    sendStroke(null, null, x, y);
});

canvas.addEventListener("touchend", () => { drawing = false; });

canvas.addEventListener("touchmove", (e) => {
    e.preventDefault();
    if (!drawing) return;
    const { x, y } = pos(e.touches[0]);
    drawSegment({ x0: lastX, y0: lastY, x1: x, y1: y, color: colorPicker.value, size: parseInt(brushSize.value) });
    sendStroke(lastX, lastY, x, y);
    lastX = x;
    lastY = y;
});

// ── Position helper ───────────────────────────────────────────
function pos(e) {
    const r = canvas.getBoundingClientRect();
    return { x: e.clientX - r.left, y: e.clientY - r.top };
}

// ── Clear ─────────────────────────────────────────────────────
function clearCanvas() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    strokeCount = 0;
    strokeEl.textContent = 0;
    if (socket && socket.readyState === WebSocket.OPEN) {
        socket.send(JSON.stringify({ type: "clear", sender: MY_ID }));
    }
    log("🗑 Canvas cleared");
}
