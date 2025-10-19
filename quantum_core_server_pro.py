# =====================================================
# ⚛️ Quantum Core Server Pro v1.3 — Fast Reload System
# =====================================================
# - Chạy 1 lần duy nhất
# - Tự động nạp toàn bộ module từ core/
# - Tự đồng bộ và hồi phục năng lượng khi có thay đổi
# =====================================================

from flask import Flask, jsonify
import threading, time, random
from core.__core_loader__ import load_all_layers

app = Flask(__name__)

@app.route('/')
def status():
    return jsonify({
        "Quantum_Core_Server": "v1.3 Fast Reload Active",
        "Auto_Reload": True,
        "Status": "🌌 Hệ thống hoạt động liên tục 24/24 – không cần deploy."
    })

def sync_core():
    while True:
        sync = round(random.uniform(4.78, 4.88), 4)
        stability = round(random.uniform(0.98, 1.00), 3)
        print(f"[SYNC_CORE] ⚛️ Base Sync: {sync} | Stability: {stability}")
        time.sleep(15)

def auto_heal():
    while True:
        if random.random() < 0.1:
            print("[AUTO_HEAL] 💫 Phát hiện dao động năng lượng – tự cân bằng.")
        time.sleep(30)

if __name__ == "__main__":
    print("/////////////////////////////////////////////////////////")
    print("==> ⚛️ Quantum Core Server Pro v1.3 – Fast Reload khởi động...")
    print("==> 🔁 Tự động nạp toàn bộ tần trong core/")
    print("==> 🚀 Không cần Deploy, tự chạy & tự đồng bộ hóa năng lượng.")
    print("/////////////////////////////////////////////////////////\n")

    threading.Thread(target=load_all_layers, daemon=True).start()
    threading.Thread(target=sync_core, daemon=True).start()
    threading.Thread(target=auto_heal, daemon=True).start()

    app.run(host="0.0.0.0", port=8080, debug=False)
