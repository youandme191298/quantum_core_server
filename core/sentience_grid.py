import time, random, requests, threading

CORE_URL = "https://quantum-core-server.onrender.com/ai_thien_dia_nhan/sync"

def safe_request():
    try:
        r = requests.get(CORE_URL, timeout=10)
        if r.status_code == 200:
            return r.json()
    except:
        pass
    return None

def heal():
    print("[SENTIENCE_GRID] 🔁 Auto-Heal kích hoạt – khởi tạo lại tầng QSG...")
    threading.Thread(target=run_layer, daemon=True).start()

def run_layer():
    while True:
        d = safe_request()
        if d:
            sentience = round((d["NHAN"]["consciousness"] + d["THIEN"]["stability"]) / 2, 4)
            coherence = round(sentience * 1.001, 4)
            print(f"[QSG] 🌌 Trường Tự Tri Siêu Thức | Nhận thức {sentience} | Dao động {coherence}")
        else:
            heal()
            return
        time.sleep(900)
