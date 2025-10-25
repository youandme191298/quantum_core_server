"""
Tầng Thiên – Quản lý năng lượng vũ trụ
"""
from core.quantum_core_server_core import quantum_log, stabilize_wave
import random, time

def get_cosmic_shift():
    """Tạo dao động năng lượng Thiên."""
    base = random.uniform(3.5, 4.5)
    shift = stabilize_wave(base, 0.2)
    quantum_log(f"☀️  Dao động Thiên giới: {shift:.4f}")
    return shift

def init_layer():
    """Khởi tạo tầng Thiên."""
    quantum_log("🌀 Kích hoạt Tầng Thiên – Năng lượng vũ trụ đang hội tụ...")
    time.sleep(0.3)
    return get_cosmic_shift()
