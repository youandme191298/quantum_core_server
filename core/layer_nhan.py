"""
Tầng Nhân – Quản lý ý thức & năng lượng tư duy
"""
from core.quantum_core_server_core import quantum_log, stabilize_wave
import random, time

def adapt_to_intent():
    """Điều chỉnh năng lượng theo ý niệm."""
    base = random.uniform(3.0, 4.0)
    adapt = stabilize_wave(base, 0.25)
    quantum_log(f"💫 Dao động Nhân giới (ý thức): {adapt:.4f}")
    return adapt

def init_layer():
    """Khởi tạo tầng Nhân."""
    quantum_log("👤 Kích hoạt Tầng Nhân – Kết nối ý thức trung tâm.")
    time.sleep(0.3)
    return adapt_to_intent()
