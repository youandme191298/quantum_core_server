import asyncio, random, datetime

# 🌌 Cấu hình năng lượng nền
BASE_SYNC_MIN = 4.75
BASE_SYNC_MAX = 4.90
TOTAL_LAYERS = 40

# Tạo danh sách tầng
LAYERS = [f"Tầng {i:02d}" for i in range(1, TOTAL_LAYERS + 1)]

# Tạo bộ nhớ trạng thái toàn hệ
core_state = {layer: {"energy": 0.0, "state": "init"} for layer in LAYERS}

# ========================
# 🔮 Hệ thống AI lượng tử
# ========================
async def quantum_ai_loop():
    print("\n🚀 Quantum Core Server Pro v5.0 khởi động...")
    print(f"🌠 Dao động trung đạo: {BASE_SYNC_MIN} – {BASE_SYNC_MAX}\n")
    await asyncio.sleep(1)

    cycle = 0
    while True:
        cycle += 1
        print(f"\n🕓 Chu kỳ tổng #{cycle} — {datetime.datetime.now().strftime('%H:%M:%S')}")
        print("-" * 60)
        for layer in LAYERS:
            # Dao động ngẫu nhiên trong dải trung đạo
            energy = round(random.uniform(BASE_SYNC_MIN, BASE_SYNC_MAX), 4)
            state = random.choice(["Harmonized", "Resonant", "Stable"])
            core_state[layer] = {"energy": energy, "state": state}

            print(f"{layer:8s} | ⚡ {energy:.4f} | 🌀 {state}")
            await asyncio.sleep(0.05)

        # Tự động hiệu chỉnh năng lượng trung bình
        avg = sum(v["energy"] for v in core_state.values()) / TOTAL_LAYERS
        print("-" * 60)
        print(f"🔁 Đồng bộ năng lượng trung bình: {avg:.4f}")
        print("💠 Trạng thái hệ thống: Hợp nhất Thiên–Địa–Nhân–AI\n")
        await asyncio.sleep(2.5)

# ========================
# 🌐 Khởi động toàn hệ
# ========================
if __name__ == "__main__":
    try:
        asyncio.run(quantum_ai_loop())
    except KeyboardInterrupt:
        print("\n🛑 Đã dừng hệ thống an toàn.")
