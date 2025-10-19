# ===============================================
# 🌌 Quantum Core Server PRO (Flask + Qiskit + AI Mode)
# -----------------------------------------------
# - Mô phỏng qubit, entanglement, Hadamard
# - API lượng tử thực
# - Quantum AI Mode tự động chạy định kỳ
# ===============================================

from flask import Flask, request, jsonify
from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
import threading
import json
import time
import os
import atexit
from datetime import datetime

# ===============================================
# ⚙️ KHỞI TẠO ỨNG DỤNG FLASK
# ===============================================
app = Flask(__name__)

# ===============================================
# 🧠 CẤU HÌNH HỆ THỐNG
# ===============================================
HISTORY_FILE = "ai_history.json"
INTERVAL_SECONDS = int(os.environ.get("QUANTUM_AI_INTERVAL", 600))
SHOTS = int(os.environ.get("QUANTUM_AI_SHOTS", 512))
MAX_HISTORY = 200

# ===============================================
# ⚛️ HÀM MÔ PHỎNG LƯỢNG TỬ
# ===============================================
def run_quantum_circuit(qc, shots=512):
    backend = Aer.get_backend("aer_simulator")
    tqc = transpile(qc, backend)
    job = backend.run(tqc, shots=shots)
    result = job.result()
    counts = result.get_counts()
    return counts

# ===============================================
# 📊 LƯU / ĐỌC LỊCH SỬ DỮ LIỆU
# ===============================================
def ensure_history_file():
    if not os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "w") as f:
            json.dump({"records": []}, f)

def read_history():
    ensure_history_file()
    with open(HISTORY_FILE, "r") as f:
        return json.load(f)

def append_history(record):
    ensure_history_file()
    with open(HISTORY_FILE, "r") as f:
        data = json.load(f)
    data["records"].append(record)
    if len(data["records"]) > MAX_HISTORY:
        data["records"] = data["records"][-MAX_HISTORY:]
    with open(HISTORY_FILE, "w") as f:
        json.dump(data, f, indent=2)

# ===============================================
# 🪐 MẠCH LƯỢNG TỬ ENTANGLEMENT
# ===============================================
def make_entangle_circuit(n_qubits):
    qc = QuantumCircuit(n_qubits, n_qubits)
    qc.h(0)
    for i in range(1, n_qubits):
        qc.cx(0, i)
    qc.measure_all()
    return qc

# ===============================================
# 🌐 API CHÍNH
# ===============================================

@app.route('/')
def home():
    return jsonify({
        "status": "online",
        "message": "Quantum Core Server PRO đang hoạt động ⚛️",
        "routes": ["/entangle?qubits=3&shots=512", "/ai/status", "/ai/run_once"]
    })


@app.route('/entangle')
def entangle():
    try:
        n = int(request.args.get('qubits', 3))
        shots = int(request.args.get('shots', 512))
        if n < 2:
            return jsonify({"error": "Số qubit tối thiểu là 2"}), 400

        qc = make_entangle_circuit(n)
        counts = run_quantum_circuit(qc, shots)

        return jsonify({
            "status": "ok",
            "qubits": n,
            "shots": shots,
            "counts": counts
        })
    except Exception as e:
        return jsonify({"status": "error", "error": str(e)})

@app.route('/status')
def status():
    return jsonify({"status": "running", "shots": SHOTS, "interval": INTERVAL_SECONDS})

# ===============================================
# 🤖 QUANTUM AI MODE — CHẠY TỰ ĐỘNG
# ===============================================
_ai_thread = None
_ai_thread_stop = threading.Event()
_ai_running = False

def ai_cycle_once():
    """Chạy 1 chu kỳ lượng tử tự động."""
    record = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "status": "error",
        "counts": None
    }
    try:
        qc = make_entangle_circuit(3)
        counts = run_quantum_circuit(qc, shots=SHOTS)
        record["status"] = "ok"
        record["counts"] = counts
    except Exception as e:
        record["error"] = str(e)
    append_history(record)
    return record

def ai_loop():
    global _ai_running
    _ai_running = True
    app.logger.info("⚙️ Quantum AI Mode bắt đầu chạy định kỳ...")
    while not _ai_thread_stop.is_set():
        ai_cycle_once()
        for _ in range(INTERVAL_SECONDS):
            if _ai_thread_stop.is_set():
                break
            time.sleep(1)
    _ai_running = False
    app.logger.info("🛑 Quantum AI Mode đã dừng.")

def start_ai_thread():
    global _ai_thread, _ai_running
    if _ai_running:
        return False
    _ai_thread_stop.clear()
    _ai_thread = threading.Thread(target=ai_loop, daemon=True)
    _ai_thread.start()
    return True

def stop_ai_thread():
    global _ai_thread_stop
    _ai_thread_stop.set()
    return True

# ===============================================
# 🌐 API QUẢN LÝ AI MODE
# ===============================================

@app.route('/ai/status', methods=['GET'])
def ai_status():
    return jsonify({"running": _ai_running, "interval": INTERVAL_SECONDS, "shots": SHOTS})

@app.route('/ai/start', methods=['GET', 'POST'])
def ai_start():
    if start_ai_thread():
        return jsonify({"status": "started", "interval": INTERVAL_SECONDS, "shots": SHOTS})
    else:
        return jsonify({"status": "already_running"})

@app.route('/ai/stop', methods=['GET', 'POST'])
def ai_stop():
    stop_ai_thread()
    return jsonify({"status": "stopping"})

@app.route('/ai/history', methods=['GET'])
def ai_history():
    return jsonify(read_history())

@app.route('/ai/run_once', methods=['GET', 'POST'])
def ai_run_once():
    """Chạy thử một vòng đo năng lượng (hỗ trợ GET để test trên trình duyệt)."""
    try:
        n = int(request.args.get("qubits", 3))
        shots = int(request.args.get("shots", SHOTS))
        if n < 2 or n > 10:
            return jsonify({"status": "error", "error": "Số qubit hợp lệ là từ 2 đến 10"}), 400
        qc = make_entangle_circuit(n)
        counts = run_quantum_circuit(qc, shots=shots)
        record = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "status": "ok",
            "qubits": n,
            "shots": shots,
            "counts": counts
        }
        append_history(record)
        return jsonify(record)
    except Exception as e:
        return jsonify({"status": "error", "error": str(e)})

# ===============================================
# 🚀 TỰ KHỞI ĐỘNG KHI DEPLOY
# ===============================================
atexit.register(lambda: stop_ai_thread())
ensure_history_file()
start_ai_thread()

# ===============================================
# 💫 CHẠY SERVER
# ===============================================
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
