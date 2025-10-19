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
    print("[SYNC_BASE] 🔁 Auto-Heal kích hoạt – tầng đang tái khởi...")
    threading.Thread(target=run_layer, daemon=True).start()

def run_layer():
    while True:
        d = safe_request()
        if d:
            sync = d['sync_level']
            print(f"[AUTO_SYNC] 🌌 Đồng bộ {sync} | Trạng thái: {d['status']}")
            print(f"[HARMONY_AI] ✨ Tự điều chỉnh năng lượng {round(sync * 1.002,4)}")
        else:
            heal()
            return
        time.sleep(600)
