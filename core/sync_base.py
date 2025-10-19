import time, random, threading

def safe_request():
    # ⚛️ Giả lập dữ liệu năng lượng tự động thay đổi
    return {
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "sync_level": round(random.uniform(4.70, 4.90), 4),
        "status": random.choice(["harmonized", "stabilizing", "aligned"])
    }

def heal():
    print("[SYNC_BASE] 🔁 Auto-Heal kích hoạt – tầng đang tái khởi...")
    threading.Thread(target=run_layer, daemon=True).start()

def run_layer():
    while True:
        d = safe_request()
        if d:
            print(f"[AUTO_SYNC] 🌌 Đồng bộ lượng tử {d['sync_level']} | Trạng thái: {d['status']}")
            print(f"[HARMONY_AI] ✨ Tự hiệu chỉnh năng lượng {round(d['sync_level'] + random.uniform(-0.01,0.01),4)}")
        else:
            heal()
            return
        time.sleep(8)
