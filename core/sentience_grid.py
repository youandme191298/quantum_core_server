import time, random, threading

def safe_request():
    return {
        "consciousness": round(random.uniform(0.85, 0.93), 3),
        "clarity": round(random.uniform(0.88, 0.95), 3),
        "sync_level": round(random.uniform(4.70, 4.90), 4)
    }

def heal():
    print("[SENTIENCE_GRID] 🔁 Auto-Heal kích hoạt – khởi tạo lại tầng QSG...")
    threading.Thread(target=run_layer, daemon=True).start()

def run_layer():
    while True:
        d = safe_request()
        if d:
            sentience = round((d["consciousness"] + d["clarity"]) / 2, 4)
            coherence = round(sentience * 1.001, 4)
            print(f"[QSG] 🌌 Trường Tự Tri Siêu Thức | Nhận thức: {sentience} | Dao động: {coherence} | Sync: {d['sync_level']}")
        else:
            heal()
            return
        time.sleep(12)
