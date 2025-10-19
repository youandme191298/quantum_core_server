from flask import Flask, request, jsonify
from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer

# ⚙️ Khởi tạo Flask app
app = Flask(__name__)

# 💡 Trạng thái hệ thống
quantum_state = {
    "status": "idle",
    "last_result": None,
    "qubits": 0,
    "shots": 0
}

# 🧭 Hàm mô phỏng mạch lượng tử
def run_quantum_circuit(qc, shots=512):
    backend = Aer.get_backend('aer_simulator')
    # Chuyển mạch sang dạng tối ưu hóa
    tqc = transpile(qc, backend)
    job = backend.run(tqc, shots=shots)
    result = job.result()
    counts = result.get_counts()
    return counts


# 🌐 Trang chủ kiểm tra server
@app.route('/')
def home():
    return jsonify({
        "status": "online",
        "message": "Quantum Core Server đang hoạt động ổn định ⚛️",
        "routes": ["/entangle?qubits=2&shots=512"]
    })


# ⚛️ API: mô phỏng trạng thái vướng víu (entanglement)
@app.route('/entangle')
def entangle():
    try:
        n = int(request.args.get('qubits', 2))
        shots = int(request.args.get('shots', 512))
        if n < 2:
            return jsonify({"error": "Số qubit tối thiểu là 2"}), 400

        # 🧩 Tạo mạch lượng tử
        qc = QuantumCircuit(n, n)
        qc.h(0)
        for i in range(1, n):
            qc.cx(0, i)
        qc.measure_all()

        counts = run_quantum_circuit(qc, shots)
        quantum_state.update({
            "status": "ok",
            "last_result": counts,
            "qubits": n,
            "shots": shots
        })

        return jsonify({
            "status": "ok",
            "qubits": n,
            "shots": shots,
            "counts": counts
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "error": str(e)
        })


# 🧪 API: kiểm tra trạng thái
@app.route('/status')
def status():
    return jsonify(quantum_state)


# 🚀 Chạy Flask (Render tự gọi khi deploy)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
