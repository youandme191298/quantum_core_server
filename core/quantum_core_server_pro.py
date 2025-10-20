# ==========================================================
# 🌌 QUANTUM CORE SERVER PRO — HỢP NHẤT THIÊN – ĐỊA – NHÂN
# Phiên bản 3.0 (Tích hợp tự động, hiển thị log năng lượng)
# ==========================================================

import time, random, datetime
from core.layer_thien import get_cosmic_shift
from core.layer_dia import stabilize_energies
from core.layer_nhan import adapt_to_intent, random_intent_wave

# ----------------------------------------------------------
# ⚙️ Cấu hình hệ thống tổng
# ----------------------------------------------------------
TOTAL_TIERS = 40                # số tầng năng lượng
UPDATE_INTERVAL = 1.2           # chu kỳ cập nhật (giây)
BASE_ENERGY = 4.8               # năng lượng nền tảng
RANDOM_VARIATION = 0.15         # dao động ban đầu ngẫu nhiên
LOG_LIMIT = 8                   # số log hiển thị mỗi chu kỳ

# Khởi tạo năng lượng tầng
energies = [BASE_ENERGY + random.uniform(-RANDOM_VARIATION, RANDOM_VARIATION)
            for _ in range(TOTAL_TIERS)]

# ----------------------------------------------------------
# 🌠 Hàm cập nhật năng lượng từng tầng
# ----------------------------------------------------------
def update_quantum_layers():
    """Cập nhật toàn bộ hệ năng lượng Thiên–Địa–Nhân."""
    global energies

    # 🌌 1. Dao động vũ trụ (Thiên Đạo)
    cosmic_shift = get_cosmic_shift()
    energies = [e + cosmic_shift for e in energies]

    # 🧠 2. Cảm ứng ý niệm (Nhân Đạo)
    intent = random_intent_wave()
    resonance = adapt_to_intent(intent)
    energies = [e + resonance for e in energies]

    # 🌍 3. Ổn định năng lượng (Địa Đạo)
    energies = stabilize_energies(energies)

    # Tính tổng và trung bình năng lượng hệ
    total_energy = sum(energies)
    avg_energy = total_energy / len(energies)
    return {
        "intent": intent,
        "resonance": resonance,
        "cosmic_shift": cosmic_shift,
        "avg_energy": avg_energy,
        "total_energy": total_energy
    }

# ----------------------------------------------------------
# 🔁 Chu kỳ chạy tự động 24/24
# ----------------------------------------------------------
def run_server():
    print("🚀 Quantum Core Server Pro đang khởi động...")
    print("🪐 Hợp nhất Thiên – Địa – Nhân, đồng bộ năng lượng lượng tử.\n")

    cycle = 0
    while True:
        cycle += 1
        stats = update_quantum_layers()
        now = datetime.datetime.now().strftime("%H:%M:%S")

        # Giới hạn hiển thị log (chỉ một phần để tránh quá tải)
        sample = [round(e, 4) for e in energies[:LOG_LIMIT]]
        print(f"[{now}] ⚙️ Chu kỳ {cycle:03d} | "
              f"Thiên {stats['cosmic_shift']:+.5f} | "
              f"Nhân {stats['resonance']:+.5f} | "
              f"Avg {stats['avg_energy']:.5f} | "
              f"Intent {stats['intent']:+.3f} | "
              f"Tầng mẫu: {sample}")

        # Tự điều chỉnh nhịp theo năng lượng tổng thể
        time.sleep(UPDATE_INTERVAL)

# ----------------------------------------------------------
# 🚀 Chạy server khi gọi trực tiếp
# ----------------------------------------------------------
if __name__ == "__main__":
    try:
        run_server()
    except KeyboardInterrupt:
        print("\n🧘 Hệ thống Quantum Core dừng lại trong cân bằng Thiên–Địa–Nhân.")
