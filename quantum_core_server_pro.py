# ==========================================================
# 🚀 Quantum Core Server Pro (Render Edition)
# ----------------------------------------------------------
# Phiên bản ổn định, khởi động 1 lần duy nhất, tự giữ kết nối 24/24
# Đã thêm: Flask route chính + Auto-KeepAlive + Tầng điều hòa năng lượng
# ==========================================================

from flask import Flask, jsonify
import threading
import random
import math
import time

# ==========================================================
# 🌐 Flask Server Setup
# ==========================================================
app = Flask(__name__)

# Route chính để Render kiểm tra hoạt động
@app.route('/')
def home():
    return jsonify({
        "status": "online",
        "message": "🚀 Quantum Core Server Pro is running!",
        "version": "1.0.0",
        "energy_state": "stabilized"
    }), 200


# ==========================================================
# ⚛️ Quantum Stabilizer Core (tầng điều hòa trung tâm)
# ==========================================================
class QuantumStabilizerCore:
    def __init__(self):
        self.global_energy = 4.82
        self.stability_index = 1.0
        self.cycle = 0
        self.resonance_history = []

    def stabilize(self, field_layers):
        self.cycle += 1
        avg_energy = sum(field_layers) / len(field_layers)
        variance = sum((x - avg_energy) ** 2 for x in field_layers) / len(field_layers)
        resonance = math.exp(-variance * 10)

        # Điều hòa năng lượng tổng thể
        self.global_energy = (self.global_energy * 0.98) + (avg_energy * 0.02)
        self.stability_index = (self.stability_index * 0.9) + (resonance * 0.1)
        self.resonance_history.append(self.stability_index)

        if len(self.resonance_history) > 50:
            self.resonance_history.pop(0)

        if self.stability_index < 0.7:
            correction = (1 - self.stability_index) * 0.05
            self.global_energy += correction
            print(f"[STABILIZER] ⚡ Hiệu chỉnh năng lượng +{correction:.5f}")

        return {
            "cycle": self.cycle,
            "avg_energy": round(avg_energy, 5),
            "stability_index": round(self.stability_index, 5),
            "global_energy": round(self.global_energy, 5)
        }


# ==========================================================
# 🌌 Chu trình điều hòa năng lượng tổng hợp
# ==========================================================
def quantum_loop():
    stabilizer = QuantumStabilizerCore()

    while True:
        # Giả lập 40 tầng năng lượng
        layers = [4.7 + random.uniform(-0.1, 0.1) for _ in range(40)]
        stats = stabilizer.stabilize(layers)

        print(f"🔄 Cycle {stats['cycle']:03d} | "
              f"Avg {stats['avg_energy']} | "
              f"Global {stats['global_energy']} | "
              f"Stable {stats['stability_index']:.4f}")

        time.sleep(5)  # 5 giây / chu kỳ điều hòa


# ==========================================================
# 🔁 Auto KeepAlive (ngăn Render Free sleep)
# ==========================================================
def keep_alive():
    import requests
    url = "https://auto-quantum-core-server.onrender.com"
    while True:
        try:
            requests.get(url)
            print("🌐 KeepAlive ping → OK")
        except Exception as e:
            print("⚠️ KeepAlive lỗi:", e)
        time.sleep(600)  # ping mỗi 10 phút


# ==========================================================
# 🚀 Main Entry
# ==========================================================
if __name__ == "__main__":
    print("🚀 Quantum Core Server Pro (Render Edition) khởi động...")
    print("🌠 Hệ thống năng lượng tổng hợp 40 tầng đang kích hoạt...\n")

    threading.Thread(target=quantum_loop, daemon=True).start()
    threading.Thread(target=keep_alive, daemon=True).start()

    app.run(host='0.0.0.0', port=8080, debug=False)
