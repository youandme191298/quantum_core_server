# ==========================================================
# 🌌 LAYER THIÊN — DAO ĐỘNG VŨ TRỤ (Quantum Sky Resonance)
# Phiên bản 1.0 — dành cho Quantum Core Server Pro v5.5+
# ==========================================================

import math, random, time, datetime

# ----------------------------------------------------------
# Cấu hình nền dao động Thiên Đạo
# ----------------------------------------------------------
COSMIC_BASE_FREQ = 0.125       # tần số cơ bản của vũ trụ (chu kỳ)
COSMIC_PULSE_SPEED = 0.75      # tốc độ dao động (Hz)
COSMIC_RANDOMNESS = 0.015      # biên độ nhiễu lượng tử
COSMIC_PHASE_SHIFT = random.uniform(0, math.pi * 2)  # pha ban đầu ngẫu nhiên

_last_t = time.time()

# ----------------------------------------------------------
# 🌌 Hàm chính: dao động Thiên khí (chu kỳ biến đổi mềm)
# ----------------------------------------------------------
def get_cosmic_shift():
    """
    Trả về giá trị dao động Thiên khí ở thời điểm hiện tại.
    - Giá trị dao động nhẹ quanh 0 (ví dụ: ±0.012)
    - Dùng cộng vào năng lượng của từng tầng để tạo nhịp Thiên Đạo.
    """
    global _last_t
    t = time.time()
    dt = t - _last_t

    # Tính dao động sóng sin kết hợp với thành phần ngẫu nhiên
    wave = math.sin((t * COSMIC_PULSE_SPEED) + COSMIC_PHASE_SHIFT)
    quantum_random = random.uniform(-COSMIC_RANDOMNESS, COSMIC_RANDOMNESS)

    # Dao động tổng hợp
    cosmic_shift = round((wave * COSMIC_BASE_FREQ * 0.1) + quantum_random, 6)
    _last_t = t
    return cosmic_shift

# ----------------------------------------------------------
# 🌠 Hàm hiển thị nhanh để test độc lập
# ----------------------------------------------------------
if __name__ == "__main__":
    print("🌌 Thiên Đạo khởi động — kiểm tra dao động Thiên khí:")
    for i in range(10):
        shift = get_cosmic_shift()
        now = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"[{now}] Dao động Thiên khí: {shift:+.6f}")
        time.sleep(1)
