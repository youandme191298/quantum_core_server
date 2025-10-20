import asyncio, random, datetime, os, sys, traceback, threading
from flask import Flask

# =====================================================
# 🌌 Quantum Core Server Pro v5.4 — One-time Build + Auto Reload
# =====================================================

TOTAL_LAYERS = 40
BASE_SYNC_MIN = 4.75
BASE_SYNC_MAX = 4.90
RESONANCE_FACTOR = 0.02
LOG_FILE = "quantum_core_log.txt"
SUMMARY_INTERVAL = 10

core_state = {f"Tầng {i:02d}": {"energy": 0.0, "state": "init"} for i in range(1, TOTAL_LAYERS + 1)}

# =====================================================
# 🧠 Ghi log & làm mới
# =====================================================
def write_log(msg):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {msg}")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {msg}\n")

def clear_log():
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)
        print("🧹 Đã làm mới quantum_core_log.txt\n")

# =====================================================
# 🔁 Hệ dao động lượng tử 40 tầng
# =====================================================
async def quantum_ai_loop():
    write_log("🚀 Quantum Core Server Pro v5.4 khởi động (One-time Build Mode)...")
    write_log(f"🌠 Dao động nền năng lượng: {BASE_SYNC_MIN} – {BASE_SYNC_MAX}\n")

    global_base = random.uniform(BASE_SYNC_MIN, BASE_SYNC_MAX)
    cycle = 0

    while True:
        try:
            cycle += 1
            now = datetime.datetime.now().strftime('%H:%M:%S')
            write_log(f"\n🕓 Chu kỳ #{cycle} — {now}")
            write_log("-" * 60)

            # Tính dao động từng tầng
            for i in range(1, TOTAL_LAYERS + 1):
                resonance_shift = random.uniform(-RESONANCE_FACTOR, RESONANCE_FACTOR)
                energy = round(global_base + resonance_shift, 4)
                energy = min(max(energy, BASE_SYNC_MIN), BASE_SYNC_MAX)

                state = (
                    "Resonant" if energy > (BASE_SYNC_MIN + BASE_SYNC_MAX) / 2 + 0.05
                    else "Harmonized" if energy < (BASE_SYNC_MIN + BASE_SYNC_MAX) / 2 - 0.05
                    else "Stable"
                )

                core_state[f"Tầng {i:02d}"] = {"energy": energy, "state": state}
                write_log(f"Tầng {i:02d} | ⚡ {energy:.4f} | 🌀 {state}")

            # Cộng hưởng & điều tiết năng lượng tổng
            avg_energy = sum(v["energy"] for v in core_state.values()) / TOTAL_LAYERS
            global_base += (avg_energy - global_base) * 0.4

            write_log("-" * 60)
            write_log(f"🔁 Năng lượng trung bình: {avg_energy:.4f}")
            write_log("💠 Trạng thái: Hợp nhất Thiên–Địa–Nhân–AI\n")

            # Tổng kết định kỳ
            if cycle % SUMMARY_INTERVAL == 0:
                max_layer = max(core_state, key=lambda l: core_state[l]["energy"])
                min_layer = min(core_state, key=lambda l: core_state[l]["energy"])
                diff = core_state[max_layer]["energy"] - core_state[min_layer]["energy"]
                write_log(f"📊 TỔNG KẾT: Mạnh nhất {max_layer} ({core_state[max_layer]['energy']}) | "
                          f"Yếu nhất {min_layer} ({core_state[min_layer]['energy']}) | Dao động: {diff:.4f}\n")

            await asyncio.sleep(1.5)

        except Exception as e:
            write_log(f"⚠️ Lỗi vòng {cycle}: {e}")
            traceback.print_exc()
            await asyncio.sleep(3)
            continue

# =====================================================
# 🌐 Flask giữ Render online
# =====================================================
app = Flask(__name__)

@app.route('/')
def index():
    avg = sum(v["energy"] for v in core_state.values()) / TOTAL_LAYERS
    max_layer = max(core_state, key=lambda l: core_state[l]["energy"])
    min_layer = min(core_state, key=lambda l: core_state[l]["energy"])
    return f"""
    <h2>🌐 Quantum Core Server v5.4 — Real-time</h2>
    <p>🔁 Năng lượng trung bình: <b>{avg:.4f}</b></p>
    <p>⚡ Mạnh nhất: {max_layer} ({core_state[max_layer]['energy']})</p>
    <p>💤 Yếu nhất: {min_layer} ({core_state[min_layer]['energy']})</p>
    <p>💠 Trạng thái: Hợp nhất Thiên–Địa–Nhân–AI</p>
    <hr>
    <p>🪶 Phiên bản: One-time Build + Auto Reload</p>
    """

# =====================================================
# ♻️ Cơ chế Auto Reload (không cần Deploy)
# =====================================================
def watch_files_and_reload():
    try:
        from watchdog.observers import Observer
        from watchdog.events import FileSystemEventHandler
    except ImportError:
        os.system("pip install watchdog")
        from watchdog.observers import Observer
        from watchdog.events import FileSystemEventHandler

    class ReloadHandler(FileSystemEventHandler):
        def on_modified(self, event):
            if event.src_path.endswith(".py"):
                print(f"\n♻️ Reload triggered by {event.src_path} — restarting server...\n")
                os.execv(sys.executable, ["python"] + sys.argv)

    observer = Observer()
    observer.schedule(ReloadHandler(), ".", recursive=True)
    observer.start()
    print("👁‍🗨 Auto-Reload đang theo dõi thay đổi mã nguồn...")

# =====================================================
# 🚀 Khởi chạy chính
# =====================================================
if __name__ == "__main__":
    clear_log()

    threading.Thread(target=lambda: app.run(host="0.0.0.0", port=8080), daemon=True).start()
    threading.Thread(target=watch_files_and_reload, daemon=True).start()

    try:
        asyncio.run(quantum_ai_loop())
    except KeyboardInterrupt:
        write_log("🛑 Đã dừng hệ thống an toàn.")
    except Exception as e:
        write_log(f"🔥 Lỗi khởi động chính: {e}")
        sys.exit(1)
