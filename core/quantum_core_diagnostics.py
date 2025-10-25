"""
Quantum Core Diagnostics Tool
------------------------------
Dùng để kiểm tra hoạt động của từng tầng:
- Thời gian nạp
- Năng lượng dao động
- Tình trạng kết nối pipeline
"""

import importlib
import time
import traceback
import os
from core.quantum_core_server_core import quantum_log

LOG_FILE = os.path.join("core", "logs", "diagnostics.log")

def test_layer(module_name):
    start = time.time()
    try:
        mod = importlib.import_module(f"core.{module_name}")
        if hasattr(mod, "init_layer"):
            mod.init_layer()
        elapsed = time.time() - start
        msg = f"✅ {module_name} hoạt động tốt ({elapsed:.3f}s)"
        print(msg)
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(msg + "\n")
    except Exception as e:
        msg = f"❌ {module_name} lỗi: {e}"
        print(msg)
        traceback.print_exc()
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(msg + "\n")

def run_diagnostics(layers):
    quantum_log("🚀 Bắt đầu kiểm tra hệ thống lượng tử...")
    for layer in layers:
        test_layer(layer)
        time.sleep(0.1)
    quantum_log("🌈 Hoàn tất kiểm tra toàn bộ tầng lượng tử.")

if __name__ == "__main__":
    # Ví dụ: chỉ test 3 tầng đầu
    test_layers = [
        "quantum_genesis_engine",
        "quantum_field_stabilizer",
        "quantum_flux_regulator"
    ]
    run_diagnostics(test_layers)
