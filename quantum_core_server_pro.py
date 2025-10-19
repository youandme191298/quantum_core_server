#!/usr/bin/env python3
"""
Quantum Core Server - PRO
- Flask web API (multi-endpoint) để chạy mô phỏng Qiskit Aer (hadamard / entangle).
- Endpoints:
    GET  /                 -> Basic info (HTML)
    GET  /quantum_test     -> Run n-qubit Hadamard + measure (params: qubits, shots)
    GET  /entangle         -> Create GHZ-like entangled state across n qubits (params: qubits, shots)
    GET  /health           -> health check
- Trả về JSON: {"status":"ok","shots":..., "counts":{...}, "backend":"aer_simulator"}
"""

from flask import Flask, request, jsonify, abort, Response
import json
import os
import traceback
from typing import Dict

# Try to import Qiskit (1.x style expected). If unavailable, return helpful error in endpoints.
try:
    from qiskit import QuantumCircuit, transpile
    from qiskit.visualization import plot_histogram  # optional, not used server-side
    from qiskit.compiler import assemble
    # qiskit-aer backend import
    try:
        from qiskit_aer import Aer  # qiskit 1.x modular Aer
    except Exception:
        # some installs expose Aer via qiskit.providers.aer
        try:
            from qiskit.providers.aer import Aer
        except Exception:
            Aer = None
except Exception as e:
    QuantumCircuit = None
    transpile = None
    Aer = None

app = Flask(__name__)

# Default safe limits
MAX_QUBITS = int(os.getenv("MAX_QUBITS", "5"))    # avoid too big circuits on free tiers
MAX_SHOTS = int(os.getenv("MAX_SHOTS", "4096"))

def get_backend_name():
    if Aer is None:
        return None
    try:
        # prefer aer_simulator
        return "aer_simulator"
    except Exception:
        return None

def run_on_backend(qc: "QuantumCircuit", shots: int = 512) -> Dict:
    """
    Compile & run circuit on Aer simulator, return counts dict.
    """
    if QuantumCircuit is None or Aer is None:
        raise RuntimeError("Qiskit / Aer not available in environment.")

    backend = Aer.get_backend(get_backend_name())
    # transpile for simulator
    compiled = transpile(qc, backend=backend)
    qobj = assemble(compiled, shots=shots)
    job = backend.run(qobj)
    result = job.result()
    counts = result.get_counts()
    return counts

def parse_positive_int(param, default, name, max_val=None):
    try:
        v = int(request.args.get(param, default))
    except Exception:
        v = default
    if v < 1:
        v = default
    if max_val is not None and v > max_val:
        v = max_val
    return v

@app.route("/")
def index():
    backend_ok = (QuantumCircuit is not None and Aer is not None)
    backend_name = get_backend_name() or "not-available"
    html = f"""
    <html>
      <head><title>Quantum Core Server — PRO</title></head>
      <body style="font-family:system-ui,Segoe UI,Roboto,Arial;">
        <h1>Quantum Core Server — PRO</h1>
        <p><b>Backend:</b> {backend_name} ({'ready' if backend_ok else 'missing'})</p>
        <p>Use <code>/quantum_test?qubits=3&shots=512</code> or
           <code>/entangle?qubits=3&shots=1024</code></p>
        <p>Health: <a href="/health">/health</a></p>
      </body>
    </html>
    """
    return Response(html, mimetype="text/html")

@app.route("/health")
def health():
    ok = (QuantumCircuit is not None and Aer is not None)
    return jsonify({"status": "ok" if ok else "error", "qiskit_available": ok})

@app.route("/quantum_test")
def quantum_test():
    """
    Build n-qubit Hadamard circuit: apply H on each qubit, then measure all.
    Params:
        qubits: int (1..MAX_QUBITS)
        shots: int (1..MAX_SHOTS)
    """
    try:
        if QuantumCircuit is None or Aer is None:
            return jsonify({"status": "error", "message": "Qiskit/Aer not available on server."}), 500

        qubits = parse_positive_int("qubits", 1, "qubits", MAX_QUBITS)
        shots = parse_positive_int("shots", 512, "shots", MAX_SHOTS)

        qc = QuantumCircuit(qubits, qubits)
        for i in range(qubits):
            qc.h(i)
        qc.barrier()
        qc.measure(range(qubits), range(qubits))

        counts = run_on_backend(qc, shots=shots)
        return jsonify({"status": "ok", "shots": shots, "counts": counts, "qubits": qubits})
    except Exception as ex:
        tb = traceback.format_exc()
        return jsonify({"status": "error", "error": str(ex), "trace": tb}), 500

@app.route("/entangle")
def entangle():
    """
    Build n-qubit GHZ-style circuit: H on qubit 0, then cascade CNOTs 0->1->2...
    Params: qubits, shots
    """
    try:
        if QuantumCircuit is None or Aer is None:
            return jsonify({"status": "error", "message": "Qiskit/Aer not available on server."}), 500

        qubits = parse_positive_int("qubits", 2, "qubits", MAX_QUBITS)
        shots = parse_positive_int("shots", 512, "shots", MAX_SHOTS)
        if qubits < 2:
            qubits = 2

        qc = QuantumCircuit(qubits, qubits)
        qc.h(0)
        for i in range(qubits - 1):
            qc.cx(i, i+1)
        qc.barrier()
        qc.measure(range(qubits), range(qubits))

        counts = run_on_backend(qc, shots=shots)
        return jsonify({"status": "ok", "shots": shots, "counts": counts, "qubits": qubits})
    except Exception as ex:
        tb = traceback.format_exc()
        return jsonify({"status": "error", "error": str(ex), "trace": tb}), 500

# Optional small utility endpoint to return plain counts for testing via curl
@app.route("/run_json", methods=["POST"])
def run_json():
    """
    POST a JSON body containing circuit specification:
    {"type": "hadamard"|"entangle", "qubits": 3, "shots": 512}
    """
    try:
        if not request.is_json:
            return jsonify({"status":"error","message":"Expect JSON body"}), 400
        body = request.get_json()
        ctype = body.get("type","hadamard")
        qubits = int(body.get("qubits", 1))
        shots = int(body.get("shots", 512))
        # route
        if ctype == "hadamard":
            # reuse endpoint logic
            with app.test_request_context(f"/quantum_test?qubits={qubits}&shots={shots}"):
                return quantum_test()
        elif ctype == "entangle":
            with app.test_request_context(f"/entangle?qubits={qubits}&shots={shots}"):
                return entangle()
        else:
            return jsonify({"status":"error","message":"unknown type"}), 400
    except Exception as ex:
        return jsonify({"status":"error","error": str(ex), "trace": traceback.format_exc()}), 500

if __name__ == "__main__":
    # When deployed in Render, it will use gunicorn or service runner; this fallback helps local testing.
    port = int(os.getenv("PORT", "8080"))
    debug = os.getenv("FLASK_DEBUG", "0") == "1"
    app.run(host="0.0.0.0", port=port, debug=debug)
