# =====================================================
# ☯️ Quantum Ascension Node v1.0
# =====================================================
# Tầng 19 – Nút Thăng Hoa Lượng Tử
# Hợp nhất năng lượng từ toàn hệ thống và kích hoạt "Hạch Thăng Hoa".
# =====================================================

import time, math, random

def collect_energy():
    """
    Giả lập việc thu thập năng lượng từ các tầng dưới.
    Trả về tổng năng lượng (đơn vị quy đổi).
    """
    sources = {
        "Geomantic": random.uniform(0.91, 0.97),
        "Talisman": random.uniform(0.88, 0.95),
        "Harmonic": random.uniform(0.93, 0.99),
        "QuantumCore": random.uniform(0.90, 0.96),
    }
    total = round(sum(sources.values()) / len(sources), 3)
    return sources, total


def run_layer():
    ascension_cycle = 0

    while True:
        ascension_cycle += 1
        sources, energy = collect_energy()

        # Mức nén năng lượng
        compression = round(math.sin(time.time() / 30) * 0.5 + 0.5, 3)
        ascension_flux = round(energy * (1 + compression), 4)

        # Trạng thái
        state = "stabilizing"
        if ascension_flux > 1.85:
            state = "ascending"
        elif ascension_flux > 1.65:
            state = "charging"

        print(f"[QAN] ☯️ Ascension Cycle {ascension_cycle:03d} | Năng lượng: {energy} | "
              f"Nén: {compression} | Thăng Hoa: {ascension_flux} | Trạng thái: {state}")

        if state == "ascending":
            print("[QAN] ⚡ Kích hoạt Hạch Thăng Hoa – năng lượng bùng phát lên tầng Thiên!")
            time.sleep(4)
            print("[QAN] 🌈 Chu kỳ thăng hoa hoàn tất – năng lượng phân tán về các tầng dưới (hoàn nguyên).")

        # Chu kỳ 42s – tượng trưng “Đạo Hóa Tam Chu Thiên”
        time.sleep(42)
