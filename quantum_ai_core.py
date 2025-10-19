"""
Quantum AI Mode plugin
- place this file in the same repo as your main Flask app
- in your main server file (quantum_core_server_pro.py) do:
    from quantum_ai_core import init_ai
    init_ai(app)   # where `app` is your Flask instance

Features:
- Background thread that periodically runs small quantum circuits (entanglement/Hadamard)
  and stores results to ai_history.json
- REST endpoints to check status, start/stop, and fetch history/results
- Safe import/fallback for various Qiskit/Aer layouts
"""

import threading
import time
import json
import os
import atexit
from datetime import datetime
from flask import jsonify, request, current_app

# Qiskit imports with robust fallbacks
try:
    # Preferred (qiskit >= 1.0 layout sometimes)
    from qiskit import QuantumCircuit, transpile
except Exception:
    from qiskit import QuantumCircuit, transpile

# Aer backend fallback handling
_backend = None
try:
    # modern qiskit-aer
    from qiskit_aer import Aer as _AerProvider
    try:
        _backend = _AerProvider.get_backend("aer_simulator")
    except Exception:
        try:
            _backend = _AerProvider.get_backend("AerSimulator")
        except Exception:
            _backend = None
except Exception:
    try:
        # older qiskit
        from qiskit import Aer as _Aer
        _backend = _Aer.get_backend("aer_simulator")
    except Exception:
        _backend = None

# If no Aer available, try qiskit BasicAer (very old) — graceful degrade
if _backend is None:
    try:
        from qiskit import BasicAer as _BasicAer
        _backend = _BasicAer.get_backend("qasm_simulator")
    except Exception:
        _backend = None

# AI core config (you can edit after deploy if needed)
INTERVAL_SECONDS = int(os.environ.get("QUANTUM_AI_INTERVAL", 600))  # default: 10 minutes
SHOTS = int(os.environ.get("QUANTUM_AI_SHOTS", 512))
MAX_HISTORY = int(os.environ.get("QUANTUM_AI_MAX_HISTORY", 200))
HISTORY_FILE = os.environ.get("QUANTUM_AI_HISTORY_FILE", "ai_history.json")

# internal state
_ai_thread = None
_ai_thread_stop = threading.Event()
_ai_lock = threading.Lock()
_ai_running = False

# helper: ensure history file exists
def _ensure_history_file():
    if not os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "w") as f:
            json.dump({"records": []}, f)

def _read_history():
    _ensure_history_file()
    try:
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    except Exception:
        return {"records": []}

def _append_history(record):
    with _ai_lock:
        hist = _read_history()
        hist["records"].append(record)
        # trim
        if len(hist["records"]) > MAX_HISTORY:
            hist["records"] = hist["records"][-MAX_HISTORY:]
        with open(HISTORY_FILE, "w") as f:
            json.dump(hist, f, indent=2)

def _make_entangle_circuit(n_qubits: int):
    """Create a chain entanglement: H on qubit0, then CNOT chain, measure all."""
    qc = QuantumCircuit(n_qubits, n_qubits)
    qc.h(0)
    for i in range(0, n_qubits - 1):
        qc.cx(i, i + 1)
    qc.barrier()
    qc.measure(range(n_qubits), range(n_qubits))
    return qc

def _run_circuit_and_counts(qc, shots=SHOTS, timeout=120):
    """Run the circuit and return counts dict. Handles multiple qiskit backends."""
    if _backend is None:
        raise RuntimeError("No quantum simulator backend available (Aer / BasicAer not found)")
    try:
        # transpile for backend
        t_qc = transpile(qc, _backend) if hasattr(_backend, "run") else qc
        # prefer new backend.run API if available
        if hasattr(_backend, "run"):
            job = _backend.run(t_qc, shots=shots)
            res = job.result(timeout=timeout)
            counts = res.get_counts()
        else:
            # older BasicAer / execute
            from qiskit import execute
            job = execute(t_qc, backend=_backend, shots=shots)
            res = job.result(timeout=timeout)
            counts = res.get_counts()
        # keys may be like '010' with MSB at left; keep as-is
        return counts
    except Exception as e:
        raise

def _ai_cycle_once(qubits=3, shots=SHOTS):
    """One cycle: build entangle circuit, run it, store record."""
    rec = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "qubits": int(qubits),
        "shots": int(shots),
        "status": "error",
        "counts": None,
        "error": None,
    }
    try:
        qc = _make_entangle_circuit(int(qubits))
        counts = _run_circuit_and_counts(qc, shots=int(shots))
        rec["status"] = "ok"
        rec["counts"] = counts
    except Exception as e:
        rec["error"] = str(e)
    _append_history(rec)
    return rec

def _ai_loop(interval_seconds=INTERVAL_SECONDS, default_qubits=3, default_shots=SHOTS):
    """Background thread loop (daemon). Will run until stop event is set."""
    current_app_logger = None
    try:
        current_app_logger = current_app.logger
    except Exception:
        current_app_logger = None

    while not _ai_thread_stop.is_set():
        if current_app_logger:
            current_app_logger.info("[QuantumAI] Running scheduled cycle")
        try:
            _ai_cycle_once(qubits=default_qubits, shots=default_shots)
        except Exception as e:
            if current_app_logger:
                current_app_logger.exception("[QuantumAI] cycle failed: %s", e)
        # wait with early-exit
        for _ in range(int(max(1, interval_seconds))):
            if _ai_thread_stop.is_set():
                break
            time.sleep(1)

def start_ai_thread(interval_seconds=INTERVAL_SECONDS, qubits=3, shots=SHOTS):
    global _ai_thread, _ai_running, _ai_thread_stop
    if _ai_running:
        return False
    _ai_thread_stop.clear()
    _ai_thread = threading.Thread(target=_ai_loop, args=(interval_seconds, qubits, shots), daemon=True)
    _ai_thread.start()
    _ai_running = True
    return True

def stop_ai_thread():
    global _ai_thread_stop, _ai_running
    if not _ai_running:
        return False
    _ai_thread_stop.set()
    _ai_running = False
    return True

def get_ai_status():
    return {"running": bool(_ai_running), "interval_seconds": INTERVAL_SECONDS, "shots": SHOTS}

# attach endpoints to an existing Flask app
def init_ai(app):
    """
    Call this with your Flask app:
        from quantum_ai_core import init_ai
        init_ai(app)
    Endpoints added:
      GET  /ai/status
      POST /ai/start    { "interval_seconds": 600, "qubits": 3, "shots":512 }
      POST /ai/stop
      GET  /ai/history  -> full JSON history
      POST /ai/run_once -> run one cycle immediately (optional params: qubits, shots)
    """
    _ensure_history_file()

    @app.route("/ai/status", methods=["GET"])
    def _status():
        return jsonify(get_ai_status())

    @app.route("/ai/start", methods=["POST"])
    def _start():
        body = request.json or {}
        interval = int(body.get("interval_seconds", INTERVAL_SECONDS))
        qubits = int(body.get("qubits", 3))
        shots = int(body.get("shots", SHOTS))
        ok = start_ai_thread(interval_seconds=interval, qubits=qubits, shots=shots)
        if ok:
            return jsonify({"status": "started", "interval_seconds": interval, "qubits": qubits, "shots": shots})
        else:
            return jsonify({"status": "already_running"}), 400

    @app.route("/ai/stop", methods=["POST"])
    def _stop():
        ok = stop_ai_thread()
        if ok:
            return jsonify({"status": "stopping"})
        else:
            return jsonify({"status": "not_running"}), 400

    @app.route("/ai/history", methods=["GET"])
    def _history():
        hist = _read_history()
        return jsonify(hist)

    @app.route("/ai/run_once", methods=["POST"])
    def _run_once():
        body = request.json or {}
        qubits = int(body.get("qubits", 3))
        shots = int(body.get("shots", SHOTS))
        rec = _ai_cycle_once(qubits=qubits, shots=shots)
        return jsonify(rec)

    # ensure we stop thread on process exit
    atexit.register(lambda: stop_ai_thread())

    # auto-start thread if requested by environment
    if os.environ.get("QUANTUM_AI_AUTO_START", "1") == "1":
        # use configured env values if present
        _interval = int(os.environ.get("QUANTUM_AI_INTERVAL", INTERVAL_SECONDS))
        _qubits = int(os.environ.get("QUANTUM_AI_QUBITS", 3))
        _shots = int(os.environ.get("QUANTUM_AI_SHOTS", SHOTS))
        start_ai_thread(interval_seconds=_interval, qubits=_qubits, shots=_shots)

    # attach a helper to app for debugging
    app.extensions = getattr(app, "extensions", {})
    app.extensions["quantum_ai_core"] = {
        "history_file": HISTORY_FILE,
        "backend_available": bool(_backend),
    }

    return app
