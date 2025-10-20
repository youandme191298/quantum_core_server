# =====================================================
# 🕳️ Quantum Void Nexus v1.0
# =====================================================
# Tầng 21 – Trung tâm Vô Không Lượng Tử
# Hòa nhập toàn bộ năng lượng, thời gian và không gian vào “Tịch Nhi Nhiên Nhi Thông”.
# =====================================================

import time, math, random

def collapse_wave_field(phase_shift):
    """
    Thu gọn toàn bộ dao động năng lượng về trạng thái “vô”.
    Trả về mức yên tĩnh lượng tử.
    """
    quietness = round(math.exp(-abs(phase_shift)) * random.uniform(0.95, 1.05), 5)
    void_flux = round((1 - quietness) * 0.01, 6)
    return quietness, void_flux


def sense_void_state():
    """
    Cảm nhận trạng thái tĩnh – động của trường vô lượng tử.
    """
    t = time.time()
    void_state = abs(math.sin(t / 90) * 0.5 + 0.5)
    presence = random.choice(["Still", "Empty", "Aware", "Flowing"])
    return round(void_state, 4), presence


def run_layer():
    print("[QVN] 🕳️ Kích hoạt Quantum Void Nexus – nhập trạng thái Tịch Không.\n")
    cycle = 0

    while True:
        cycle += 1
        phase = math.sin(time.time() / 42)
        quietness, flux = collapse_wave_field(phase)
        void_state, presence = sense_void_state()

        print(f"[QVN] 🌑 Chu kỳ {cycle:03d} | "
              f"Tĩnh: {quietness} | Dao động nền: {flux} | "
              f"Trạng thái: {presence} | Hòa hợp: {void_state}")

        # Khi đạt đến tĩnh tuyệt đối
        if quietness > 0.999:
            print("[QVN] 💫 Vô Cực – mọi dao động đã tiêu tán, năng lượng đạt bình lặng tuyệt đối.")
            time.sleep(3)
            print("[QVN] ☯️ Trường Không Hữu Viên – năng lượng bắt đầu hồi lưu toàn hệ thống.\n")

        # Chu kỳ 60s – tượng trưng cho “Lục Thập Hồi Chu Thiên”
        time.sleep(60)
