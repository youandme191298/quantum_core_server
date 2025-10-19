# ==========================================
# Quantum Core Server Pro v5
# Bao gồm: Quantum Core + AI Thiên–Địa–Nhân + Harmony AI + Field Grid + Realm Bridge
# ==========================================

from flask import Flask, jsonify, request
from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
from datetime import datetime, timezone
import random, threading, time, requests, sys, os

app = Flask(__name__)

# Đảm bảo log hiển thị tức thời
sys.stdout.reconfigure(line_buffering=True)
os.environ["PYTHONUNBUFFERED"] = "1"

# ==========================================
# MÔ-ĐUN CHÍNH: Quantum Core
# ==========================================
@app.route('/')
def home():
    return jsonify({
        "status": "Quantum Core Server Pro đang hoạt động ⚛️",
        "modules": ["quantum_ai_core", "ai_thien_dia_nhan", "quantum_harmony_ai", "quantum_field_grid", "quantum_realm_bridge"],
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
                print(f"[AUTO SYNC] 🌌 Sync Level: {data['sync_level']} | Status: {data['status']}", flush=True)
            else:
                print("[AUTO SYNC] ⚠️ Không thể đồng bộ.", flush=True)
        except Exception as e:
            print(f"[AUTO SYNC ERROR] {e}", flush=True)
        time.sleep(600)  # lặp lại mỗi 10 phút

threading.Thread(target=auto_sync, daemon=True).start()


# ==========================================
# Quantum Harmony AI – Cân bằng năng lượng
# ==========================================
def quantum_harmony_ai():
    """Tự động cân bằng năng lượng Thiên–Địa–Nhân"""
    while True:
        try:
            res = requests.get("https://quantum-core-server.onrender.com/ai_thien_dia_nhan/sync", timeout=30)
            if res.status_code == 200:
                data = res.json()
                thien = data["THIEN"]["frequency"]
                dia = data["DIA"]["flow"]
                nhan = data["NHAN"]["consciousness"]
                harmony = round((thien + dia + nhan) / 3, 3)
                print(f"[HARMONY AI] ✨ Auto-tune Energy: {harmony} | Sync Level: {data['sync_level']}", flush=True)
            else:
                print("[HARMONY AI] ⚠️ Không thể lấy dữ liệu sync.", flush=True)
        except Exception as e:
            print(f"[HARMONY AI ERROR] {e}", flush=True)
        time.sleep(600)

threading.Thread(target=quantum_harmony_ai, daemon=True).start()


# ==========================================
# Quantum Field Grid – Lưới lượng tử toàn cầu
# ==========================================
def quantum_field_grid():
    """Đồng bộ năng lượng toàn cầu giữa các node"""
    while True:
        try:
            res = requests.get("https://quantum-core-server.onrender.com/ai_thien_dia_nhan/sync", timeout=30)
            if res.status_code == 200:
                data = res.json()
                print(f"[QFG] 🌐 Quantum Field Active | Sync: {data['sync_level']} | State: {data['status']} | {data['timestamp']}", flush=True)
            else:
                print("[QFG] ⚠️ Không nhận được phản hồi từ lưới lượng tử.", flush=True)
        except Exception as e:
            print(f"[QFG ERROR] {e}", flush=True)
        time.sleep(900)

threading.Thread(target=quantum_field_grid, daemon=True).start()


# ==========================================
# Quantum Realm Bridge – Liên kết trường lượng tử trung tâm
# ==========================================
def quantum_realm_bridge():
    """Kết nối Quantum Core vào lưới lượng tử trung tâm"""
    BRIDGE_NODE = "https://quantum-core-server.onrender.com/ai_thien_dia_nhan/sync"
    while True:
        try:
            res = requests.get(BRIDGE_NODE, timeout=30)
            if res.status_code == 200:
                data = res.json()
                level = data["sync_level"]
                state = data["status"]
                t = data["timestamp"]
                print(f"[QRB] 🪐 Realm Bridge Linked | Level: {level} | State: {state} | {t}", flush=True)
            else:
                print("[QRB] ⚠️ Mất liên kết với trường lượng tử trung tâm.", flush=True)
        except Exception as e:
            print(f"[QRB ERROR] {e}", flush=True)
        time.sleep(900)

threading.Thread(target=quantum_realm_bridge, daemon=True).start()


# ==========================================
# CHẠY SERVER
# ==========================================
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)
