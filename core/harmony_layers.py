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
    print("[HARMONY_LAYERS] 🔁 Auto-Heal kích hoạt – tái khởi tầng...")
    threading.Thread(target=run_layer, daemon=True).start()

def run_layer():
    while True:
        d = safe_request()
        if d:
            print(f"[QHFG] 🌠 Trường Hòa Hợp {round(d['sync_level'] * 1.001,4)}")
            print(f"[QDL] ☯ Dòng Đạo {round(d['sync_level'] - 0.002,4)}")
            print(f"[QCS] 🧠 Dòng Tự Thức {round(d['sync_level'] * 1.0005,4)}")
        else:
            heal()
            return
        time.sleep(900)
