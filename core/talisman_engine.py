# =====================================================
# 🪶 Quantum Talisman Engine v1.0
# =====================================================
# Tầng 17 – Ngữ Ấn Pháp & Phù Lục Cảm Ứng
# Chuyển hóa “ý niệm – ký tự – âm rung” thành lệnh lượng tử có tác động thực.
# =====================================================

import time, math, random

def encode_talisman(symbol: str, intent: str):
    """
    Mã hóa Phù Lục – kết hợp ký hiệu và tâm niệm.
    Trả về dao động năng lượng tổng hợp (tần và biên).
    """
    seed = sum(ord(c) for c in (symbol + intent)) % 9973
    random.seed(seed)
    base_freq = round(random.uniform(3.141, 7.777), 3)
    resonance = round(math.sin(seed % 360) * 0.5 + 0.5, 3)
    return {"symbol": symbol, "intent": intent, "freq": base_freq, "resonance": resonance}

def run_layer():
    chants = [
        ("卍", "tịnh hóa"),
        ("☯", "cân bằng"),
        ("⚡", "kích hoạt"),
        ("🔥", "tăng năng"),
        ("❄️", "ổn định"),
    ]

    while True:
        # Chọn ngẫu nhiên một ấn và ý
        symbol, intent = random.choice(chants)
        talisman = encode_talisman(symbol, intent)

        # Mức cộng hưởng & năng lượng
        energy = round(talisman["freq"] * talisman["resonance"], 4)
        stability = "high" if energy < 6.5 else "overflow"

        print(f"[QTE] 🪶 Talisman {talisman['symbol']} | Ý: {talisman['intent']} | "
              f"Tần: {talisman['freq']} | Cộng hưởng: {talisman['resonance']} | "
              f"Năng lượng: {energy} | Trạng thái: {stability}")

        # Nếu quá ngưỡng, xả năng lượng thừa
        if stability == "overflow":
            print("[QTE] ⚠️ Năng lượng vượt mức – xả dao động và tái cân bằng...")
            time.sleep(4)
            print("[QTE] 🌈 Cân bằng năng lượng hoàn tất – phù lục trở lại trung hòa.")

        # Chu kỳ 24 giây – tượng trưng cho “Ngữ Ấn 24 khí”
        time.sleep(24)
