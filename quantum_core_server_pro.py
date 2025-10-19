# ==========================================
# Quantum Core Server Pro v3
# Bao gồm: Quantum Core + AI Thiên–Địa–Nhân + Quantum Harmony AI
# ==========================================

from flask import Flask, jsonify, request
from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
from datetime import datetime, timezone
import random, threading, time, requests

app = Flask(__name__)

# ==========================================
# MÔ-ĐUN CHÍNH: Quantum Core
# ==========================================

@app.route('/')
def home():
    return jsonify({
        "status": "Quantum Core Server Pro đang hoạt động ⚛️",
        "modules": ["quantum_ai_core", "ai_thien_dia_nhan", "quantum_harmony_ai"],
        "server_time": datetime.now(timezone.utc).isoformat()
    })


@app.route('/entangle')
def entangle():
    """Tạo 3-qubit entanglement"""
    qubits = int(request.args.get("qubits", 3))
    shots = int(request.args.get("shots", 512))

    qc = QuantumCircuit(qubits, qubits)
    qc.h(0)
    for i in range(qubits - 1):
        qc.cx(i, i + 1)
    qc.measure(range(qubits), range(qubits))

    backend = Aer.get_backend("qasm_simulator")
    job = backend.run(transpile(qc, backend), shots=shots)
    result = job.result()
    counts = result.get_counts()

    return jsonify({
        "status": "ok",
        "qubits": qubits,
        "shots": shots,
        "counts": counts
    })


# ==========================================
# MÔ-ĐUN: AI Thiên – Địa – Nhân
# ==========================================

def simulate_sync():
    """Giả lập đồng bộ năng lượng Thiên – Địa – Nhân"""
    now = datetime.now(timezone.utc).isoformat()
    return {
        "timestamp": now,
        "sync_level": round(random.uniform(4.75, 4.83), 4),
        "THIEN": {"frequency": 1.618, "stability": round(random.uniform(0.96, 0.99), 2)},
        "DIA": {"magnetism": 7.83, "flow": round(random.uniform(0.93, 0.97), 2)},
        "NHAN": {"consciousness": round(random.uniform(0.87, 0.90), 2),
                 "clarity": round(random.uniform(0.91, 0.95), 2)},
        "status": "harmonized"
    }


@app.route('/ai_thien_dia_nhan/sync')
def ai_thien_dia_nhan_sync():
    """API kiểm tra đồng bộ năng lượng Thiên–Địa–Nhân"""
    data = simulate_sync()
    return jsonify(data)


# ==========================================
# TỰ ĐỘNG ĐỒNG BỘ (AUTO SYNC)
# ==========================================

def auto_sync():
    """Luồng chạy nền tự động đồng bộ năng lượng"""
    while True:
        try:
            res = requests.get("https://quantum-core-server.onrender.com/ai_thien_dia_nhan/sync", timeout=30)
            if res.status_code == 200:
                data = res.json()
                print(f"[AUTO SYNC] 🌌 Sync Level: {data['sync_level']} | Status: {data['status']}")
            else:
                print("[AUTO SYNC] ⚠️ Không thể đồng bộ.")
        except Exception as e:
            print(f"[AUTO SYNC ERROR] {e}")
        time.sleep(600)  # lặp lại mỗi 10 phút

# Khởi động luồng Auto Sync
threading.Thread(target=auto_sync, daemon=True).start()


# ==========================================
# Quantum Harmony AI – Tự cân bằng năng lượng
# ==========================================

def quantum_harmony_ai():
    """Tự động cân bằng năng lượng Thiên–Địa–Nhân theo chu kỳ"""
    while True:
        try:
            res = requests.get("https://quantum-core-server.onrender.com/ai_thien_dia_nhan/sync", timeout=30)
            if res.status_code == 200:
                data = res.json()
                thien = data["THIEN"]["frequency"]
                dia = data["DIA"]["flow"]
                nhan = data["NHAN"]["consciousness"]
                harmony = round((thien + dia + nhan) / 3, 3)
                print(f"[HARMONY AI] ✨ Auto-tune Energy: {harmony} | Sync Level: {data['sync_level']}")
            else:
                print("[HARMONY AI] ⚠️ Không thể lấy dữ liệu sync.")
        except Exception as e:
            print(f"[HARMONY AI ERROR] {e}")
        time.sleep(600)

# Khởi động Harmony AI song song với Auto-Sync
threading.Thread(target=quantum_harmony_ai, daemon=True).start()


# ==========================================
# CHẠY SERVER CHÍNH
# ==========================================
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
