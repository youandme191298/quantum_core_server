# ==========================================
# Quantum Modular Core v12.5
# Modular Loader + Auto-Heal Engine
# ==========================================

from flask import Flask, jsonify
import importlib, os, threading, time, sys
from datetime import datetime, timezone

sys.stdout.reconfigure(line_buffering=True)
app = Flask(__name__)

# ==========================================
# MODULE DISCOVERY ENGINE
# ==========================================
CORE_PATH = "core"
ACTIVE_MODULES = {}

def load_module(module_name):
    try:
        module = importlib.import_module(f"{CORE_PATH}.{module_name}")
        threading.Thread(target=module.run_layer, daemon=True).start()
        ACTIVE_MODULES[module_name] = "active"
        print(f"[LOADER] ✅ Đã nạp tầng {module_name.upper()}", flush=True)
    except Exception as e:
        ACTIVE_MODULES[module_name] = f"error: {e}"
        print(f"[LOADER] ⚠️ Lỗi khi nạp tầng {module_name}: {e}", flush=True)

def auto_load_modules():
    for file in os.listdir(CORE_PATH):
        if file.endswith(".py") and not file.startswith("__"):
            module_name = file[:-3]
            load_module(module_name)

# ==========================================
# FLASK STATUS & API
# ==========================================
@app.route('/')
def home():
    return jsonify({
        "status": "Quantum Modular Core v12.5 ⚛️ Live",
        "modules": list(ACTIVE_MODULES.keys()),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "note": "Hệ thống đang tự động duy trì các tầng năng lượng lượng tử."
    })

@app.route('/modules')
def modules():
    return jsonify(ACTIVE_MODULES)

# ==========================================
# AUTO RELOADER (10 phút quét lại module mới)
# ==========================================
def module_watcher():
    known = set(ACTIVE_MODULES.keys())
    while True:
        time.sleep(600)
        current = {f[:-3] for f in os.listdir(CORE_PATH) if f.endswith(".py")}
        new = current - known
        for module in new:
            print(f"[WATCHER] 🔄 Phát hiện module mới: {module}, đang nạp...")
            load_module(module)
            known.add(module)

# ==========================================
# MAIN STARTUP
# ==========================================
if __name__ == "__main__":
    print("⚛️ Quantum Modular Core khởi động...")
    auto_load_modules()
    threading.Thread(target=module_watcher, daemon=True).start()
    app.run(host="0.0.0.0", port=8080, debug=False)
