# Quantum Core Server Pro v5.5 — Unified + Visualizer
# Paste nguyên khối này vào quantum_core_server_pro.py và save.

import asyncio, random, datetime, os, sys, traceback, threading, json
from flask import Flask, jsonify, Response

# =========================
# Config
# =========================
TOTAL_LAYERS = 40
BASE_SYNC_MIN = 4.75
BASE_SYNC_MAX = 4.90
RESONANCE_FACTOR = 0.02
LOG_FILE = "quantum_core_log.txt"
SUMMARY_INTERVAL = 10
AUTO_RELOAD_ENABLED = True

# =========================
# State
# =========================
LAYERS = [f"Tầng {i:02d}" for i in range(1, TOTAL_LAYERS + 1)]
core_state = {layer: {"energy": 0.0, "state": "init"} for layer in LAYERS}
cycle_counter = {"value": 0}

# =========================
# Logging utilities
# =========================
def write_log(msg):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] {msg}"
    print(line)
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(line + "\n")
    except Exception:
        pass

def clear_log():
    if os.path.exists(LOG_FILE):
        try:
            os.remove(LOG_FILE)
            print("🧹 Đã làm mới quantum_core_log.txt")
        except Exception:
            pass

# =========================
# Core quantum loop
# =========================
async def quantum_ai_loop():
    write_log("🚀 Quantum Core Server Pro v5.5 khởi động (Visualizer Enabled)")
    write_log(f"🌠 Dao động nền năng lượng: {BASE_SYNC_MIN} – {BASE_SYNC_MAX}\n")
    await asyncio.sleep(0.5)

    global_base = random.uniform(BASE_SYNC_MIN, BASE_SYNC_MAX)

    while True:
        try:
            cycle_counter["value"] += 1
            cycle = cycle_counter["value"]
            now = datetime.datetime.now().strftime('%H:%M:%S')
            write_log(f"\n🕓 Chu kỳ #{cycle} — {now}")
            write_log("-" * 60)

            # update each layer
            energies = []
            for i, layer in enumerate(LAYERS):
                resonance_shift = random.uniform(-RESONANCE_FACTOR, RESONANCE_FACTOR) * (1 + i / TOTAL_LAYERS)
                energy = round(global_base + resonance_shift, 4)
                energy = min(max(energy, BASE_SYNC_MIN), BASE_SYNC_MAX)

                midpoint = (BASE_SYNC_MIN + BASE_SYNC_MAX) / 2.0
                if energy > midpoint + 0.05:
                    state = "Resonant"
                elif energy < midpoint - 0.05:
                    state = "Harmonized"
                else:
                    state = "Stable"

                core_state[layer] = {"energy": energy, "state": state}
                energies.append(energy)
                write_log(f"{layer:8s} | ⚡ {energy:.4f} | 🌀 {state}")

            # adjust global base by partial convergence to average
            avg = sum(energies) / TOTAL_LAYERS
            global_base += (avg - global_base) * 0.4

            write_log("-" * 60)
            write_log(f"🔁 Năng lượng trung bình: {avg:.4f}")
            write_log("💠 Trạng thái: Hợp nhất Thiên–Địa–Nhân–AI\n")

            # periodic summary
            if cycle % SUMMARY_INTERVAL == 0:
                max_layer = max(core_state, key=lambda l: core_state[l]["energy"])
                min_layer = min(core_state, key=lambda l: core_state[l]["energy"])
                diff = core_state[max_layer]["energy"] - core_state[min_layer]["energy"]
                write_log(f"📊 TỔNG KẾT: Mạnh nhất {max_layer} ({core_state[max_layer]['energy']}) | "
                          f"Yếu nhất {min_layer} ({core_state[min_layer]['energy']}) | Dao động: {diff:.4f}\n")

            # short sleep to keep cycle reasonable
            await asyncio.sleep(1.0)

        except Exception as e:
            err = traceback.format_exc()
            write_log(f"⚠️ Lỗi trong chu kỳ {cycle}: {e}\n{err}")
            await asyncio.sleep(3)
            continue

# =========================
# Flask web + visualizer
# =========================
app = Flask(__name__)

@app.route('/')
def index():
    # minimal page with a canvas and JS that polls /status
    html = f"""
    <!doctype html>
    <html>
    <head>
      <meta charset="utf-8">
      <title>Quantum Core Server v5.5</title>
      <style>
        body{{font-family: Arial, sans-serif; background:#0b1020; color:#e6eef8;}}
        .wrap{{width:1000px; max-width:95%; margin:20px auto;}}
        h1{{margin:0 0 8px 0; font-size:20px;}}
        .meta{{margin-bottom:12px; color:#9fb3d3;}}
        canvas{{background:#051225; border-radius:6px; display:block; margin-top:12px;}}
        .info{{margin-top:10px; color:#cde;}}
      </style>
    </head>
    <body>
      <div class="wrap">
        <h1>🌐 Quantum Core Server v5.5 — Visualizer</h1>
        <div class="meta">Status: <span id="status">starting...</span> | Cycle: <span id="cycle">0</span></div>
        <canvas id="chart" width="960" height="360"></canvas>
        <div class="info">
          <span id="summary"></span>
        </div>
      </div>

      <script>
        const canvas = document.getElementById('chart');
        const ctx = canvas.getContext('2d');
        const W = canvas.width, H = canvas.height;
        const layers = {len_layers};
        const barW = Math.floor(W / layers) - 4;

        function draw(stateObj) {{
          // clear
          ctx.fillStyle = '#03111b';
          ctx.fillRect(0,0,W,H);

          // draw bars
          const maxVal = {base_max};
          const minVal = {base_min};
          const range = maxVal - minVal;

          let i = 0;
          for (const k of Object.keys(stateObj)) {{
            const v = stateObj[k];
            const energy = v.energy;
            const normalized = (energy - minVal) / range;
            const barH = Math.max(4, Math.floor(normalized * (H-40)));
            const x = i * (barW + 4) + 20;
            const y = H - barH - 30;

            // color by state
            let color = '#66c2a5';
            if (v.state === 'Resonant') color = '#ff8a65';
            else if (v.state === 'Harmonized') color = '#7f7fff';

            // draw bar
            ctx.fillStyle = color;
            ctx.fillRect(x, y, barW, barH);

            // label
            ctx.fillStyle = '#bcd';
            ctx.font = '11px monospace';
            ctx.fillText(k.split(' ')[1], x, H - 12);

            i++;
          }}

          // footer line
          ctx.strokeStyle = '#1f3b4b';
          ctx.beginPath();
          ctx.moveTo(0, H-28);
          ctx.lineTo(W, H-28);
          ctx.stroke();
        }}

        async function fetchStatus() {{
          try {{
            const res = await fetch('/status');
            const j = await res.json();
            document.getElementById('status').innerText = j.status;
            document.getElementById('cycle').innerText = j.cycle;
            document.getElementById('summary').innerText = `Avg: ${j.avg.toFixed(4)} | Max: ${j.max_layer} (${j.max_val}) | Min: ${j.min_layer} (${j.min_val})`;
            draw(j.state);
          }} catch (e) {{
            console.error(e);
            document.getElementById('status').innerText = 'error';
          }}
        }}

        // poll every 1000ms
        setInterval(fetchStatus, 1000);
        // initial
        fetchStatus();
      </script>
    </body>
    </html>
    """.format(len_layers=len(LAYERS), base_max=BASE_SYNC_MAX, base_min=BASE_SYNC_MIN)
    return Response(html, mimetype="text/html")

@app.route('/status')
def status():
    # prepare lightweight JSON snapshot
    try:
        snapshot = {layer: {"energy": core_state[layer]["energy"], "state": core_state[layer]["state"]} for layer in LAYERS}
        avg = round(sum(core_state[l]["energy"] for l in LAYERS) / TOTAL_LAYERS, 4)
        max_layer = max(LAYERS, key=lambda l: core_state[l]["energy"])
        min_layer = min(LAYERS, key=lambda l: core_state[l]["energy"])
        return jsonify({
            "status": "running",
            "cycle": cycle_counter["value"],
            "avg": avg,
            "max_layer": max_layer,
            "min_layer": min_layer,
            "max_layer": max_layer,
            "max_val": core_state[max_layer]["energy"],
            "min_val": core_state[min_layer]["energy"],
            "state": snapshot
        })
    except Exception as e:
        return jsonify({"status": "error", "error": str(e)}), 500

# =========================
# Auto-reload watcher (fast restart using exec)
# =========================
def start_watchdog():
    if not AUTO_RELOAD_ENABLED:
        return

    try:
        from watchdog.observers import Observer
        from watchdog.events import FileSystemEventHandler
    except Exception:
        # try to install watchdog if missing (only first-time)
        try:
            os.system(f"{sys.executable} -m pip install watchdog -q")
            from watchdog.observers import Observer
            from watchdog.events import FileSystemEventHandler
        except Exception as e:
            write_log(f"⚠️ Không thể cài watchdog: {e}")
            return

    class Handler(FileSystemEventHandler):
        def on_modified(self, event):
            if event.src_path.endswith(".py"):
                write_log(f"♻️ File modified: {event.src_path} — restarting process...")
                # restart process (exec)
                os.execv(sys.executable, [sys.executable] + sys.argv)

    obs = Observer()
    obs.schedule(Handler(), path='.', recursive=True)
    obs.daemon = True
    obs.start()
    write_log("👁 Auto-Reload watcher đã khởi động (theo dõi .py)")

# =========================
# Run
# =========================
def start_flask():
    # bind to 0.0.0.0:8080 so Render sees it as web service
    app.run(host="0.0.0.0", port=8080)

if __name__ == "__main__":
    # clear old log on start
    clear_log()

    # start flask in background thread
    threading.Thread(target=start_flask, daemon=True).start()

    # start watchdog to allow live edit without redeploy
    start_watchdog()

    # run async core loop (blocks main thread)
    try:
        asyncio.run(quantum_ai_loop())
    except KeyboardInterrupt:
        write_log("🛑 Đã dừng hệ thống an toàn.")
    except Exception as e:
        write_log(f"🔥 Lỗi khởi động chính: {e}")
        sys.exit(1)
