from flask import Flask, request, jsonify
from qiskit import QuantumCircuit, Aer, execute
import threading, time, random

app = Flask(__name__)

quantum_state = {
    "energy": 0.0,
    "layer": "Heaven",
    "status": "idle",
    "cycles": 0
}

@app.route('/')
def home():
    return jsonify({
        "status": "online",
        "energy": quantum_state["energy"],
        "layer": quantum_state["layer"],
        "message": "🌌 Quantum Core active — Render layer operational 24/24"
    })

@app.route('/activate', methods=['POST'])
def activate_layer():
    data = request.get_json(force=True)
    layer = data.get("layer", "Heaven")
    shots = int(data.get("shots", 512))

    qc = QuantumCircuit(1, 1)
    qc.h(0)
    qc.measure(0, 0)

    backend = Aer.get_backend("aer_simulator")
    result = execute(qc, backend, shots=shots).result()
    counts = result.get_counts()

    energy = round((counts.get('1', 0) / shots), 3)
    quantum_state.update({
        "energy": energy,
        "layer": layer,
        "status": "active",
        "cycles": quantum_state["cycles"] + 1
    })

    return jsonify({
        "message": f"🔹 Activated layer: {layer}",
        "quantum_energy": energy,
        "counts": counts,
        "total_cycles": quantum_state["cycles"]
    })

@app.route('/status')
def status():
    return jsonify(quantum_state)

def auto_stabilize():
    while True:
        time.sleep(90)
        quantum_state["energy"] = round(random.uniform(0.4, 0.95), 3)
        quantum_state["cycles"] += 1

threading.Thread(target=auto_stabilize, daemon=True).start()

if __name__ == '__main__':
    print("🚀 Quantum Core Server is starting on port 8080...")
    app.run(host='0.0.0.0', port=8080)
