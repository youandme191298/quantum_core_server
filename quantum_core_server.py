# ============================================================
# 🌌 Quantum Core Server - Flask + Qiskit Aer (24/24)
# Tác giả: ChatGPT Quantum Bootstrap Assistant
# Mô phỏng mạch lượng tử Hadamard và API Flask công khai
# ============================================================

from flask import Flask, request, jsonify
from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer

# ------------------------------------------------------------
# 🚀 Khởi tạo Flask App
# ------------------------------------------------------------
app = Flask(__name__)

@app.route('/')
def home():
    return "🧠 Quantum Core Server đang hoạt động ổn định 24/24 ⚛️"

# ------------------------------------------------------------
# 🔮 QUANTUM TEST ENDPOINT
# ------------------------------------------------------------
@app.route("/quantum_test", methods=["GET"])
def quantum_test():
    """
    API mô phỏng mạch lượng tử Hadamard.
    Sử dụng Qiskit Aer backend để chạy ảo qubit.
    URL ví dụ:
        /quantum_test
        /quantum_test?shots=1024
    """
    try:
        # số lần đo qubit (mặc định 512)
        shots = int(request.args.get("shots", 512))

        # Tạo mạch lượng tử 1 qubit
        qc = QuantumCircuit(1, 1)
        qc.h(0)              # cổng Hadamard
        qc.measure(0, 0)     # đo qubit

        # Backend mô phỏng lượng tử (Aer)
        backend = Aer.get_backend("aer_simulator")

        # Biên dịch và chạy
        compiled = transpile(qc, backend)
        result = backend.run(compiled, shots=shots).result()
        counts = result.get_counts()

        # Trả về JSON kết quả
        return jsonify({
            "status": "ok",
            "shots": shots,
            "counts": counts
        })

    except Exception as e:
        # Bắt lỗi và phản hồi dạng JSON
        return jsonify({
            "status": "error",
            "message": str(e)
        })

# ------------------------------------------------------------
# 🔁 Chạy server Flask (Render sẽ tự khởi động cổng 8080)
# ------------------------------------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
