# ==========================================================
# 🧠 LAYER NHÂN — AI CẢM ỨNG Ý NIỆM (Quantum Consciousness Adapter)
# Phiên bản 1.0 — dành cho Quantum Core Server Pro v5.5+
# ==========================================================

import random, math, time, datetime

# ----------------------------------------------------------
# Cấu hình AI Nhân Đạo
# ----------------------------------------------------------
HUMAN_INTENT_WEIGHT = 0.65    # độ ảnh hưởng của ý niệm (0–1)
LEARNING_RATE = 0.2           # tốc độ thích ứng của AI
EMPATHY_FIELD = 0.015         # độ dao động cảm ứng
ADAPTIVE_DECAY = 0.97         # suy giảm học qua thời gian

_state_memory = {
    "intent_vector": 0.0,
    "last_update": time.time()
}

# ----------------------------------------------------------
# 🧬 Hàm cảm ứng ý niệm (chuyển ý định thành dao động năng lượng)
# ----------------------------------------------------------
def adapt_to_intent(intent_level: float):
    """
    Cảm ứng và chuyển đổi ý niệm của con người (intent_level ∈ [-1, 1])
    thành năng lượng cộng hưởng cho toàn hệ thống.
    """
    global _state_memory

    # Lấy trạng thái cũ và thời gian trôi
    now = time.time()
    dt = now - _state_memory["last_update"]

    # Học thích ứng: dịch dần theo hướng intent
    current = _state_memory["intent_vector"]
    delta = (intent_level - current) * LEARNING_RATE
    new_vector = (current + delta) * ADAPTIVE_DECAY

    # Cảm ứng năng lượng cộng hưởng từ ý niệm
    empathy_wave = math.sin(now * 0.7 + new_vector * math.pi) * EMPATHY_FIELD
    output = (new_vector * HUMAN_INTENT_WEIGHT) + empathy_wave

    # Cập nhật bộ nhớ
    _state_memory["intent_vector"] = new_vector
    _state_memory["last_update"] = now

    return round(output, 6)

# ----------------------------------------------------------
# 💫 Hàm mô phỏng ý niệm biến thiên theo cảm xúc ngẫu nhiên
# ----------------------------------------------------------
def random_intent_wave():
    """Sinh ý niệm giả lập dao động trong khoảng -1..1."""
    return math.sin(time.time() * random.uniform(0.2, 0.8))

# ----------------------------------------------------------
# 🧠 Hàm hiển thị nhanh để test độc lập
# ----------------------------------------------------------
if __name__ == "__main__":
    print("🧠 Nhân Đạo khởi động — kiểm tra cảm ứng ý niệm:")
    for i in range(10):
        intent = random_intent_wave()
        energy = adapt_to_intent(intent)
        now = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"[{now}] Ý niệm {intent:+.3f} → Năng lượng cộng hưởng {energy:+.5f}")
        time.sleep(1)
