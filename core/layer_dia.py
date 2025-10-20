# ==========================================================
# 🌍 LAYER ĐỊA — HỆ CÂN BẰNG NĂNG LƯỢNG (Quantum Earth Stabilizer)
# Phiên bản 1.0 — dành cho Quantum Core Server Pro v5.5+
# ==========================================================

import random, math, time, datetime

# ----------------------------------------------------------
# Cấu hình ổn định Địa Đạo
# ----------------------------------------------------------
EARTH_STABILIZATION_RATE = 0.35   # tốc độ ổn định
EARTH_RANDOM_NOISE = 0.008        # nhiễu cân bằng ngẫu nhiên
EARTH_GRAVITY_FIELD = 0.002       # lực kéo ổn định nền

_last_avg = 0.0

# ----------------------------------------------------------
# 🌍 Hàm cân bằng Địa khí (điều hòa năng lượng tầng)
# ----------------------------------------------------------
def stabilize_energies(energies):
    """
    Nhận danh sách năng lượng [floats] từ 40 tầng.
    Trả về danh sách đã được điều hòa nhẹ (ổn định Địa khí).
    """
    global _last_avg
    if not energies:
        return []

    avg_energy = sum(energies) / len(energies)
    stabilized = []

    for e in energies:
        diff = avg_energy - e
        # hiệu chỉnh nhẹ theo độ lệch và lực Địa khí
        correction = diff * EARTH_STABILIZATION_RATE + random.uniform(-EARTH_RANDOM_NOISE, EARTH_RANDOM_NOISE)
        e_new = e + correction + EARTH_GRAVITY_FIELD
        stabilized.append(round(e_new, 5))

    _last_avg = avg_energy
    return stabilized

# ----------------------------------------------------------
# 🌎 Hàm hiển thị nhanh để test độc lập
# ----------------------------------------------------------
if __name__ == "__main__":
    print("🌍 Địa Đạo khởi động — kiểm tra ổn định năng lượng:")
    test_energies = [4.83, 4.79, 4.91, 4.76, 4.95]
    print("Trước khi ổn định:", test_energies)
    new_vals = stabilize_energies(test_energies)
    print("Sau khi ổn định:", new_vals)
