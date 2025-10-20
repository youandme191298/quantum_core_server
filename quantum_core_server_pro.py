# ==========================================================
# 🚀 Quantum Core Server Pro (Render Edition)
# ----------------------------------------------------------
# Phiên bản ổn định + Entanglement Grid (Tầng 41)
# Hợp nhất 40 tầng năng lượng – tự cân bằng – giữ sống 24/24
# ==========================================================

from flask import Flask, jsonify
import threading
import random
import math
import time
import requests

# ==========================================================
# 🌐 Flask Server
# ==========================================================
app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "status": "online",
        "message": "🚀 Quantum Core Server Pro + QEG running!",
        "version": "1.1.0",
        "energy_state": "Unified Resonance Active"
    }), 200


# ==========================================================
# ⚛️ Quantum Stabilizer Core (40 tầng điều hòa)
# ==========================================================
class QuantumStabilizerCore:
    def __init__(self):
        self.global_energy = 4.82
        self.stability_index = 1.0
        self.cycle = 0
        self.entanglement_memory = []

    def stabilize(self, field_layers):
        self.cycle += 1
        avg_energy = sum(field_layers) / len(field_layers)
        variance = sum((x - avg_energy) ** 2 for x in field_layers) / len(field_layers)
        resonance = math.exp(-variance * 10)

        self.global_energy = (self.global_energy * 0.98) + (avg_energy * 0.02)
        self.stability_index = (self.stability_index * 0.9) + (resonance * 0.1)

        # Lưu lịch sử năng lượng cho QEG
        self.entanglement_memory.append({
            "cycle": self.cycle,
            "energy": self.global_energy,
            "resonance": self.stability_index
        })
        if len(self.entanglement_memory) > 60:
            self.entanglement_memory.pop(0)

        return {
            "cycle": self.cycle,
            "avg_energy": round(avg_energy, 5),
            "stability_index": round(self.stability_index, 5),
            "global_energy": round(self.global_energy, 5)
        }


# ==========================================================
# 🌐 Quantum Entanglement Grid (Tầng 41)
# ==========================================================
class QuantumEntanglementGrid:
    def __init__(self):
        self.entropy_level = 0.01
        self.sync_strength = 1.0
        self.last_energy_field = None

    def unify(self, stabilizer: QuantumStabilizerCore):
        if not stabilizer.entanglement_memory:
            return None

        # Phân tích dao động 5 chu kỳ gần nhất
        recent = stabilizer.entanglement_memory[-5:]
        avg_energy = sum(e["energy"] for e in recent) / len(recent)
        avg_resonance = sum(e["resonance"] for e in recent) / len(recent)

        # Cân bằng tần số hợp nhất
        coherence = (avg_resonance + stabilizer.stability_index) / 2
        delta = abs(avg_energy - stabilizer.global_energy)
        self.sync_strength = max(0.8, 1 - delta * 5)

        unified_energy = (avg_energy * coherence * self.sync_strength)
        self.last_energy_field = unified_energy

        print(f"[QEG⚡] Unified Field → {unified_energy:.5f} | Sync {self.sync_strength:.3f} | Coherence {coherence:.3f}")
        return unified_energy


# ==========================================================
# 🌌 Chu trình lượng tử tổng hợp
# ==========================================================
def quantum_loop():
    stabilizer = QuantumStabilizerCore()
    qeg = QuantumEntanglementGrid()

    while True:
        # 40 tầng năng lượng mô phỏng
        layers = [4.7 + random.uniform(-0.1, 0.1) for _ in range(40)]
        stats = stabilizer.stabilize(layers)
        unified = qeg.unify(stabilizer)

        print(f"🔄 Cycle {stats['cycle']:03d} | "
              f"Avg {stats['avg_energy']} | "
              f"Global {stats['global_energy']} | "
              f"Stable {stats['stability_index']:.4f}")

        time.sleep(5)


# ==========================================================
# 🛰️ KeepAlive (ngăn Render sleep)
# ==========================================================
def keep_alive():
    url = "https://auto-quantum-core-server.onrender.com"
    while True:
        try:
            requests.get(url)
            print("🌐 KeepAlive ping → OK")
        except Exception as e:
            print("⚠️ KeepAlive lỗi:", e)
        time.sleep(600)


# ==========================================================
# 🚀 Main Entry
# ==========================================================
if __name__ == "__main__":
    print("🚀 Quantum Core Server Pro + QEG (Tầng 41) khởi động...")
    print("🌠 Hệ thống năng lượng hợp nhất Thiên – Địa – Nhân đang kích hoạt...\n")

    threading.Thread(target=quantum_loop, daemon=True).start()
    threading.Thread(target=keep_alive, daemon=True).start()

    app.run(host='0.0.0.0', port=8080, debug=False)
