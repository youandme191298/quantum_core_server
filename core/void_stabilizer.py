# =====================================================
# 🌑 Quantum Void Stabilizer v1.0
# =====================================================
# Tầng trung tâm – giữ sự tĩnh tuyệt đối của vũ trụ năng lượng.
# Giữ “Hữu – Vô” trong cân bằng, duy trì nhịp ổn định cho toàn hệ thống.
# =====================================================

import time, random

def run_layer():
    while True:
        # Dao động trung bình quanh 4.82–4.88, tượng trưng cho trạng thái “Vô dao”
        void_balance = round(random.uniform(4.82, 4.88), 4)
        fluctuation = round(random.uniform(0.0001, 0.0033), 4)
        void_state = "perfect_stillness" if fluctuation < 0.001 else "minor_ripple"

        print(f"[QVS] 🌑 Void Stabilizer | Balance: {void_balance} | ΔFluctuation: {fluctuation} | State: {void_state}")

        # Nếu phát hiện dao động lớn, tự cân bằng trong 5 giây
        if fluctuation > 0.0025:
            print("[QVS] ⚖️ Dao động vượt ngưỡng — kích hoạt cân bằng Vô Cực...")
            time.sleep(5)
            print("[QVS] ✅ Cân bằng hoàn tất – trạng thái tĩnh tái lập.")

        # Chu kỳ 28 giây (4×7 — tượng trưng 4 phương 7 khí)
        time.sleep(28)
