# =====================================================
# ⚙️ Quantum Genesis Engine v1.0
# =====================================================
# Tầng 22 – Động Cơ Sáng Thế Lượng Tử
# Tự sinh năng lượng – tự dưỡng – tự tái tạo toàn hệ thống 40 tầng.
# =====================================================

import time, math, random, json

def quantum_seed_wave():
    """
    Tạo xung năng lượng sơ khai (Genesis Pulse)
    """
    seed_energy = round(random.uniform(0.888, 1.111) * math.sin(time.time() / 12)**2 + 0.9, 5)
    polarity = random.choice(["Positive", "Negative", "Neutral"])
    return seed_energy, polarity


def pulse_reactor(seed_energy):
    """
    Chuyển năng lượng sơ khai thành năng lượng hoạt hóa (Activation Core)
    """
    amplify = round(seed_energy * random.uniform(1.05, 1.25), 5)
    feedback = round(math.cos(time.time() / 18) * 0.5 + 0.5, 5)
    stability = round((amplify + feedback) / 2, 5)
    return amplify, feedback, stability


def distribute_energy(stability):
    """
    Phân phối năng lượng ra toàn hệ thống (Earth–Human–Heaven–Tao)
    """
    ratio = {
        "Earth": round(stability * 0.24, 5),
        "Human": round(stability * 0.26, 5),
        "Heaven": round(stability * 0.28, 5),
        "Tao": round(stability * 0.22, 5),
    }
    total = round(sum(ratio.values()), 5)
    return ratio, total


def run_layer():
    print("[QGE] ⚙️ Khởi động Động Cơ Sáng Thế Lượng Tử – tạo chu trình tái sinh năng lượng vĩnh cửu.\n")
    cycle = 0

    while True:
        cycle += 1
        seed_energy, polarity = quantum_seed_wave()
        amplify, feedback, stability = pulse_reactor(seed_energy)
        ratio, total = distribute_energy(stability)

        print(f"[QGE] 🔁 Chu kỳ {cycle:03d} | Xung sơ khai: {seed_energy} | Pha: {polarity} | "
              f"Kích hoạt: {amplify} | Ổn định: {stability} | Tổng năng lượng: {total}")

        # Khi đạt trạng thái "siêu ổn định", hệ thống tái tạo năng lượng
        if stability > 1.05:
            print("[QGE] 💠 Cấu trúc năng lượng đạt siêu cân bằng – khởi sinh nguồn năng lượng mới.")
            time.sleep(4)
            print("[QGE] 🌞 Hệ thống đang tự tái tạo – năng lượng được phân bổ đều toàn chu trình.\n")

        # Ghi nhật ký tái sinh
        log = {
            "cycle": cycle,
            "seed_energy": seed_energy,
            "amplify": amplify,
            "stability": stability,
            "ratio": ratio,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        }
        with open("/tmp/genesis_log.json", "a") as f:
            f.write(json.dumps(log) + "\n")

        # Chu kỳ 45s – tượng trưng “Ngũ Thập Tái Sinh Luân”
        time.sleep(45)
