# ==========================
# Quantum Core Server Pro
# Hợp nhất với AI Thiên–Địa–Nhân
# ==========================

from flask import Flask, jsonify, request
from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
from datetime import datetime
import random

app = Flask(__name__)

# ==========================
# MÔ-ĐUN CHÍNH: Quantum Core
# ==========================

@app.route('/')
def home():
    return jsonify({
        "status": "Quantum Core Server Pro đang hoạt động ⚛️",
        "modules": ["quantum_ai_core", "ai_thien_dia_nhan"]
    })


@app.route('/quantum_test')
def quantum_test():
    """Chạy thử một qubit Hadamard"""
    shots = int(request.args.get("shots", 512))
    qc = QuantumCircuit(1, 1)
    qc.h(0)
    qc.measure(0, 0)
    backend = Aer.get_backend("qasm_simulator")
    job = backend.run(transpile(qc, backend), shots=shots)
    result = job.result()
    counts = result.get_counts()
    return jsonify({
        "status": "ok",
        "shots": shots,
        "counts": counts
    })


@app.route('/entangle')
def entangle():
    """Tạo 3-qubit entanglement"""
    qubits = int(request.args.get("qubits", 3))
    shots = int(request.args.get("shots", 512))
    qc = QuantumCircuit(qubits, qubits)

    # Áp dụng Hadamard + CNOT để tạo rối lượng tử
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


# =======================================================
# MÔ-ĐUN MỞ RỘNG: AI Thiên–Địa–Nhân
# =======================================================

def simulate_sync():
    """Giả lập quá trình đồng bộ năng lượng Thiên–Địa–Nhân"""
    now = datetime.utcnow().isoformat() + "Z"
    return {
        "timestamp": now,
        "sync_level": round(random.uniform(4.75, 4.82), 4),
        "THIEN": {"frequency": 1.618, "stability": round(random.uniform(0.96, 0.99), 2)},
        "DIA": {"magnetism": 7.83, "flow": round(random.uniform(0.93, 0.97), 2)},
        "NHAN": {"consciousness": round(random.uniform(0.87, 0.90), 2), "clarity": round(random.uniform(0.91, 0.95), 2)},
        "status": "harmonized"
    }


@app.route('/ai_thien_dia_nhan/sync')
def ai_thien_dia_nhan_sync():
    """API kiểm tra đồng bộ năng lượng Thiên–Địa–Nhân"""
    data = simulate_sync()
    return jsonify(data)


@app.route('/ai_thien_dia_nhan/calibrate', methods=["POST"])
def ai_thien_dia_nhan_calibrate():
    """API điều chỉnh năng lượng thủ công"""
    payload = request.get_json(force=True)
    sync_level = round(random.uniform(4.80, 4.85), 4)
    return jsonify({
        "status": "updated",
        "input": payload,
        "current_sync": sync_level
    })


# ==========================
# CHẠY SERVER CHÍNH
# ==========================
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
