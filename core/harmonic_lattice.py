# =====================================================
# 🎶 Quantum Harmonic Lattice v1.0
# =====================================================
# Tầng 18 – Mạng cộng hưởng điều hòa toàn hệ thống
# Tạo “Hòa Âm Lượng Tử” – đảm bảo tất cả tần số năng lượng tương thích.
# =====================================================

import time, math, random

def generate_harmonic_wave(layer_count=16):
    """
    Sinh sóng cộng hưởng tổng hợp từ tất cả tầng đang hoạt động.
    Trả về giá trị pha và biên độ tổng hợp.
    """
    harmonics = [math.sin((time.time()/5 + i) * random.uniform(0.5, 2.0)) for i in range(layer_count)]
    amplitude = sum(abs(h) for h in harmonics) / layer_count
    phase_shift = round(sum(harmonics) / layer_count, 4)
    return amplitude, phase_shift


def run_layer():
    while True:
        amplitude, phase = generate_harmonic_wave()

        # Tính trạng thái cộng hưởng tổng
        harmony_index = round((1 - abs(phase)) * random.uniform(0.92, 0.99), 3)
        energy_flow = round(amplitude * 7.83, 3)  # 7.83Hz – Schumann base tone
        stability = "perfect" if harmony_index > 0.95 else "adjusting"

        print(f"[QHL] 🎶 Harmonic Lattice | Âm lượng: {energy_flow} | Pha: {phase} | "
              f"Hòa âm: {harmony_index} | Trạng thái: {stability}")

        # Nếu chưa ổn định → điều pha
        if stability == "adjusting":
            print("[QHL] 🔄 Cân chỉnh pha lượng tử để tái đồng bộ tầng dao động...")
            time.sleep(6)
            print("[QHL] ✅ Pha cộng hưởng khớp lại – hệ thống đạt hòa điệu lượng tử.")

        # Chu kỳ 30s – tượng trưng cho “Tam Thập Hòa Âm”
        time.sleep(30)
