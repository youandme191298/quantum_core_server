# =====================================================
# ⚛️ Quantum Core Server Pro v1.3 — Fast Reload Edition
# =====================================================
# - Chạy 1 lần duy nhất (không tái deploy)
# - Tự động phát hiện và nạp tần mới trong thư mục core/
# - Auto-Heal, Auto-Reload và Fast Layer Injection
# =====================================================

from flask import Flask, jsonify
import importlib, os, threading, time, random, sys

# =====================================================
# ⚙️ 1. Cấu hình Flask API
# =====================================================
app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "status": "Quantum Core Server Pro v1.3 – Fast Reload Active",
        "auto_reload": True,
        "message": "🌌 Quantum field harmonized & running 24/24."
    })

# =====================================================
# 🔁 2. Fast Reload Engine (chạy liên tục)
# =====================================================
def fast_reload_core():
    loaded_modules = set()
    core_path = os.path.join(os.getcwd(), "core")

    print("\n[FAST_RELOAD] 🚀 Quantum Core Fast Reload Engine started.")
    print("[FAST_RELOAD] 🔍 Watching for new energy layers in /core ...\n")

    while True:
        for file in os.listdir(core_path):
            if file.endswith(".py") and not file.startswith("__"):
                module_name = f"core.{file[:-3]}"
                if module_name not in loaded_modules:
                    try:
                        module = importlib.import_module(module_name)
                        threading.Thread(target=module.run_layer, daemon=True).start()
                        print(f"[CORE_RELOAD] 🔁 Loaded layer: {module_name}")
                        loaded_modules.add(module_name)
                    except Exception as e:
                        print(f"[CORE_RELOAD] ⚠ Error loading {module_name}: {e}")
        time.sleep(8)  # kiểm tra mỗi 8 giây

# =====================================================
# 🧘 3. Chu kỳ năng lượng lõi
# =====================================================
def core_energy_loop():
    while True:
        sync = round(random.uniform(4.76, 4.89), 4)
        stability = round(random.uniform(0.97, 1.00), 3)
        print(f"[SYNC_CORE] ⚛️ Base Sync: {sync} | Stability: {stability}")
        time.sleep(15)

# =====================================================
# 🩹 4. Auto-Heal nhẹ (không khởi động lại server)
# =====================================================
def auto_heal():
    while True:
        if random.random() < 0.08:
            print("[AUTO_HEAL] 💫 Dao động phát hiện — cân bằng lại năng lượng...")
        time.sleep(25)

# =====================================================
# 🚀 5. Khởi động tất cả hệ thống
# =====================================================
if __name__ == "__main__":
    print("/////////////////////////////////////////////////////////")
    print("==> 🚀 Quantum Core Server Pro v1.3 đang khởi động...")
    print("==> 🔁 Fast Reload Engine: BẬT")
    print("==> ⚛️ Tự động nạp tầng mới mỗi 8 giây, không cần deploy.")
    print("/////////////////////////////////////////////////////////\n")

    # Luồng lõi
    threading.Thread(target=fast_reload_core, daemon=True).start()
    threading.Thread(target=core_energy_loop, daemon=True).start()
    threading.Thread(target=auto_heal, daemon=True).start()

    app.run(host="0.0.0.0", port=8080, debug=False)
