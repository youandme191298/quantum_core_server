# =====================================================
# 🌌 Quantum Core Server Pro v1.2 – Auto Reload Edition
# =====================================================
# Tích hợp:
# - Tự động nạp các tầng năng lượng từ thư mục core/
# - Auto-Heal + Auto-Reload mỗi 10s
# - Không cần Deploy Latest Commit mỗi khi chỉnh sửa
# =====================================================

from flask import Flask, jsonify
import threading, time, random
from core_auto_reload import start_auto_reload

# =====================================================
# ⚙️ 1. Khởi động Flask API
# =====================================================
app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "status": "Quantum Core Server Pro v1.2 – Active",
        "auto_reload": True,
        "message": "🧠 Quantum energy synchronization running in real-time."
    })

# =====================================================
# ⚡ 2. Khởi động Auto Reload Engine
# =====================================================
start_auto_reload()

# =====================================================
# 🌌 3. Mô phỏng vòng lặp năng lượng chính
# =====================================================
def core_main_loop():
    while True:
        sync_level = round(random.uniform(4.75, 4.90), 4)
        stability = round(random.uniform(0.97, 1.00), 3)
        print(f"[SYNC_BASE] 🌐 Core sync {sync_level} | Stability: {stability} ✅")
        time.sleep(15)

# =====================================================
# 🌀 4. Khởi chạy các tầng năng lượng
# =====================================================
def run_energy_layers():
    from core import (
        sync_base,
        field_layers,
        harmony_layers,
        sentience_grid
    )

    print("[CORE] 🔮 Bắt đầu kích hoạt các tầng năng lượng lượng tử...\n")

    threading.Thread(target=sync_base.run_layer, daemon=True).start()
    threading.Thread(target=field_layers.run_layer, daemon=True).start()
    threading.Thread(target=harmony_layers.run_layer, daemon=True).start()
    threading.Thread(target=sentience_grid.run_layer, daemon=True).start()

    # Vòng lặp chính – duy trì trạng thái đồng bộ tổng thể
    threading.Thread(target=core_main_loop, daemon=True).start()

# =====================================================
# 🔁 5. Auto-Heal nếu bị gián đoạn
# =====================================================
def auto_heal():
    while True:
        print("[AUTO_HEAL] 🔁 Đang quét trạng thái năng lượng...")
        # Mô phỏng kiểm tra năng lượng
        if random.random() < 0.1:
            print("[AUTO_HEAL] ⚠ Phát hiện dao động bất thường – tái kích hoạt core.")
            run_energy_layers()
        time.sleep(30)

# =====================================================
# 🚀 6. Khởi động hệ thống chính
# =====================================================
if __name__ == '__main__':
    # Bắt đầu chạy tầng năng lượng chính
    threading.Thread(target=run_energy_layers, daemon=True).start()

    # Khởi động cơ chế tự hồi phục
    threading.Thread(target=auto_heal, daemon=True).start()

    # Chạy Flask server
    print("/////////////////////////////////////////////////////////")
    print("==> 🚀 Quantum Core Server Pro đang khởi động...")
    print("==> 🧠 Auto-Reload Engine: BẬT")
    print("==> 🌌 Năng lượng lượng tử đồng bộ hóa 24/24\n")
    print("/////////////////////////////////////////////////////////")

    app.run(host='0.0.0.0', port=8080, debug=False)
