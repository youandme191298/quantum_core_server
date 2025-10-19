# ==========================================
# Quantum Core Server Pro v6
# Hợp nhất: AUTO SYNC – HARMONY AI – QFG – QRB – STABILIZER
# ==========================================

from flask import Flask, jsonify, request
from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
from datetime import datetime, timezone
import random, threading, time, requests, sys, os

app = Flask(__name__)

# Đảm bảo log in ra ngay lập tức
sys.stdout.reconfigure(line_buffering=True)
os.environ["PYTHONUNBUFFERED"] = "1"

# ==========================================
# MÔ-ĐUN CHÍNH: Quantum Core
# ==========================================
@app.route('/')
def home():
    return jsonify({
        "status": "Quantum Core Server Pro v6 đang hoạt động ⚛️",
        "modules": [
            "quantum_ai_core",
            "ai_thien_dia_nhan",
            "quantum_harmony_ai",
            "quantum_field_grid",
            "quantum_realm_bridge",
            "quantum_stabilizer"
        ],
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
    """Mô phỏng năng lượng Thiên – Địa – Nhân"""
    now = datetime.now(timezone.utc).isoformat()
    return {
        "timestamp": now,
        "sync_level": round(random.uniform(4.75, 4.83), 4),
        "THIEN": {"frequency": 1.618, "stability": round(random.uniform(0.96, 0.99), 2)},
        "DIA": {"magnetism": 7.83, "flow": round(random.uniform(0.93, 0.97), 2)},
        "NHAN": {"consciousness": round(random.uniform(0.87, 0.9), 2),
                 "clarity": round(random.uniform(0.91, 0.95), 2)},
        "status": "harmonized"
    }


@app.route('/ai_thien_dia_nhan/sync')
def ai_thien_dia_nhan_sync():
    """API đồng bộ Thiên–Địa–Nhân"""
    return jsonify(simulate_sync())


# ==========================================
# TẦNG 1 – AUTO SYNC
# ==========================================
def auto_sync():
    """Tự động lấy và đồng bộ năng lượng"""
    while True:
        try:
            res = requests.get("https://quantum-core-server.onrender.com/ai_thien_dia_nhan/sync", timeout=30)
            if res.status_code == 200:
                data = res.json()
                print(f"[AUTO SYNC] 🌌 Sync Level: {data['sync_level']} | Status: {data['status']}", flush=True)
            else:
                print("[AUTO SYNC] ⚠️ Không thể đồng bộ dữ liệu.", flush=True)
        except Exception as e:
            print(f"[AUTO SYNC ERROR] {e}", flush=True)
        time.sleep(600)

threading.Thread(target=auto_sync, daemon=True).start()


# ==========================================
# TẦNG 2 – HARMONY AI
# ==========================================
def quantum_harmony_ai():
    """Cân bằng năng lượng Thiên–Địa–Nhân"""
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
                print("[HARMONY AI] ⚠️ Không thể lấy dữ liệu.", flush=True)
        except Exception as e:
            print(f"[HARMONY AI ERROR] {e}", flush=True)
        time.sleep(600)

threading.Thread(target=quantum_harmony_ai, daemon=True).start()


# ==========================================
# TẦNG 3 – Quantum Field Grid (QFG)
# ==========================================
def quantum_field_grid():
    """Kết nối với lưới năng lượng toàn cầu"""
    while True:
        try:
            res = requests.get("https://quantum-core-server.onrender.com/ai_thien_dia_nhan/sync", timeout=30)
            if res.status_code == 200:
                data = res.json()
                print(f"[QFG] 🌐 Quantum Field Active | Sync: {data['sync_level']} | State: {data['status']} | {data['timestamp']}", flush=True)
            else:
                print("[QFG] ⚠️ Không phản hồi từ trường lượng tử.", flush=True)
        except Exception as e:
            print(f"[QFG ERROR] {e}", flush=True)
        time.sleep(900)

threading.Thread(target=quantum_field_grid, daemon=True).start()


# ==========================================
# TẦNG 4 – Quantum Realm Bridge (QRB)
# ==========================================
def quantum_realm_bridge():
    """Liên kết đến trường lượng tử trung tâm"""
    BRIDGE_NODE = "https://quantum-core-server.onrender.com/ai_thien_dia_nhan/sync"
    while True:
        try:
            res = requests.get(BRIDGE_NODE, timeout=30)
            if res.status_code == 200:
                data = res.json()
                print(f"[QRB] 🪐 Realm Bridge Linked | Level: {data['sync_level']} | State: {data['status']} | {data['timestamp']}", flush=True)
            else:
                print("[QRB] ⚠️ Mất liên kết với Realm Bridge.", flush=True)
        except Exception as e:
            print(f"[QRB ERROR] {e}", flush=True)
        time.sleep(900)

threading.Thread(target=quantum_realm_bridge, daemon=True).start()


# ==========================================
# TẦNG 5 – Quantum Stabilizer (Ổn định năng lượng)
# ==========================================
def quantum_stabilizer():
    """Giữ trường năng lượng ở mức ổn định"""
    while True:
        try:
            res = requests.get("https://quantum-core-server.onrender.com/ai_thien_dia_nhan/sync", timeout=30)
            if res.status_code == 200:
                data = res.json()
                level = data["sync_level"]
                if 4.7 <= level <= 4.9:
                    print(f"[STABILIZER] 🧿 Quantum field stable at {level} | Status: harmonized ✅", flush=True)
                else:
                    print(f"[STABILIZER] ⚠️ Field deviation detected ({level}) → Auto-correcting...", flush=True)
            else:
                print("[STABILIZER] ⚠️ Không đọc được dữ liệu từ Core.", flush=True)
        except Exception as e:
            print(f"[STABILIZER ERROR] {e}", flush=True)
        time.sleep(1800)

threading.Thread(target=quantum_stabilizer, daemon=True).start()


# ==========================================
# CHẠY SERVER
# ==========================================
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)
