"""
Tầng Địa – Quản lý năng lượng vật chất & ổn định hệ trường
"""
from core.quantum_core_server_core import quantum_log, stabilize_wave
import random, time

def stabilize_energies():
    """Cân bằng năng lượng Địa."""
    base = random.uniform(2.8, 3.8)
    stable = stabilize_wave(base, 0.15)
    quantum_log(f"🌍 Dao động Địa giới: {stable:.4f}")
    return stable

def init_layer():
    """Khởi tạo tầng Địa."""
    quantum_log("🌏 Kích hoạt Tầng Địa – Năng lượng vật chất ổn định.")
    time.sleep(0.3)
    return stabilize_energies()
