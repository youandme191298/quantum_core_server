import time, random, threading

def safe_request():
    return {
        "sync_level": round(random.uniform(4.70, 4.90), 4),
        "resonance": round(random.uniform(4.75, 4.85), 4),
        "clarity": round(random.uniform(0.88, 0.94), 3)
    }

def heal():
    print("[HARMONY_LAYERS] 🔁 Auto-Heal kích hoạt – tái khởi tầng...")
    threading.Thread(target=run_layer, daemon=True).start()

def run_layer():
    while True:
        d = safe_request()
        if d:
            print(f"[QHFG] 🌠 Trường Hòa Hợp | Năng lượng: {d['sync_level']} | Dao động: {d['resonance']}")
            print(f"[QDL] ☯ Dòng Đạo Lưu | Mức cân bằng: {round((d['sync_level'] + d['resonance'])/2,4)}")
            print(f"[QCS] 🧠 Dòng Tự Thức | Độ sáng tâm: {d['clarity']}")
        else:
            heal()
            return
        time.sleep(10)
