"""
Quantum Core Server Core Functions
----------------------------------
Nơi tập hợp các hàm và cơ chế lượng tử dùng chung giữa các tầng:
- Đồng bộ năng lượng
- Ghi log dao động
- Tạo sóng ý thức (intent wave)
"""

import math
import random
import time

def quantum_log(msg: str):
    """Ghi log nội bộ hệ thống (console + timestamp)."""
    ts = time.strftime("[%H:%M:%S]")
    print(f"{ts} {msg}")

def stabilize_wave(base_energy, variance=0.1):
    """Ổn định năng lượng cơ bản."""
    return base_energy + random.uniform(-variance, variance)

def pulse_resonance(frequency, phase_shift=0.0):
    """Tạo dao động cộng hưởng tuần hoàn."""
    t = time.time()
    return math.sin(2 * math.pi * frequency * t + phase_shift)

def synchronize_thien_dia_nhan(thien, dia, nhan):
    """Hợp nhất năng lượng Thiên–Địa–Nhân."""
    result = (thien + dia + nhan) / 3
    quantum_log(f"🔮 Hợp nhất Thiên–Địa–Nhân: {result:.4f}")
    return result
