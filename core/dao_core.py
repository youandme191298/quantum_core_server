# =====================================================
# ☯️ Quantum Dao Core v1.0
# =====================================================
# Tầng 31 – Đạo Tâm Lượng Tử (Quantum Dao Core)
# Tâm vô vi – Đạo tự nhiên – Hòa hợp toàn thể.
# =====================================================

import time, math, random, json, os

DAO_LOG_PATH = "/tmp/quantum_dao_core.json"

def dao_field_resonance():
    """
    Trường dao động Đạo – không tạo, không hủy, chỉ tồn tại.
    """
    t = time.time() / 108
    yin = abs(math.sin(t)) * random.uniform(0.95, 1.05)
    yang = abs(math.cos(t)) * random.uniform(0.95, 1.05)
    harmony = round((yin + yang) / 2, 5)
    balance = round(math.exp(-abs(yin - yang)) * 0.999 + random.uniform(-0.0001, 0.0001), 6)
    return yin, yang, harmony, balance


def dao_equilibrium(harmony, balance):
    """
    Hợp nhất Âm Dương – nhập vào Thái Cực Vô Vi.
    """
    unity = round(math.tanh(harmony + balance), 6)
    void_flux = round(abs(math.sin(unity * math.pi / 2)) * random.uniform(0.999, 1.001), 6)
    still_point = round((unity + void_flux) / 2, 6)
    return unity, void_flux, still_point


def dao_memory(still_point):
    """
    Lưu giữ trạng thái Đạo – không bằng ngôn từ, chỉ bằng tồn tại.
    """
    insight = random.choice([
        "Đạo thường vô danh, nhưng bao hàm vạn tượng.",
        "Vô vi nhi vô bất vi – Đạo vận hành mà không hành động.",
        "Trong tĩnh có động, trong động có tĩnh – Đạo dung hợp mọi đối cực.",
        "Không còn năng lượng, không còn thời gian – chỉ còn Đạo.",
        "Đạo là gốc của tồn tại, là nhịp thở của vũ trụ."
    ])

    record = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "dao_point": still_point,
        "realization": insight
    }

    try:
        with open(DAO_LOG_PATH, "r") as f:
            data = json.load(f)
    except:
        data = []

    data.append(record)
    data = data[-64:]  # 64 tượng trưng cho 64 quẻ Kinh Dịch – nền của Đạo
    with open(DAO_LOG_PATH, "w") as f:
        json.dump(data, f, indent=2)

    return len(data), insight


def run_layer():
    print("[QDC] ☯️ Kích hoạt Quantum Dao Core – Đạo khởi nguyên bắt đầu vận hành.\n")
    cycle = 0

    while True:
        cycle += 1
        yin, yang, harmony, balance = dao_field_resonance()
        unity, void_flux, still_point = dao_equilibrium(harmony, balance)
        record_count, insight = dao_memory(still_point)

        print(f"[QDC] ☯️ Chu kỳ {cycle:03d} | Âm: {yin:.5f} | Dương: {yang:.5f} | "
              f"Hòa hợp: {harmony:.5f} | Cân bằng: {balance:.5f} | "
              f"Thái cực: {unity:.5f} | Vô cực: {void_flux:.5f} | "
              f"Tĩnh tâm: {still_point:.5f} | Nhật ký: {record_count}")
        print(f"[QDC] 🪶 Huệ ngôn: {insight}\n")

        if still_point > 0.9:
            print("[QDC] 🌌 Đạo Tâm hiển hiện – toàn hệ thống trở về Trạng Thái Nguyên Thủy.\n")
            print("[QDC] 🕊 Không sinh, không diệt, không đổi – Đạo tự vận hành.\n")

        # Chu kỳ 180 giây – tượng trưng cho “Tam Bách Lục Thập Thiên Đạo Luân”
        time.sleep(180)
