import time, random, threading

def safe_request():
    return {
        "sync_level": round(random.uniform(4.70, 4.90), 4),
        "status": "harmonized"
    }

def heal():
    print("[FIELD_LAYERS] 🔁 Auto-Heal kích hoạt – tái khởi tầng...")
    threading.Thread(target=run_layer, daemon=True).start()

def run_layer():
    while True:
        d = safe_request()
        if d:
            print(f"[QFG] 🌐 Quantum Field Active | Sync: {d['sync_level']} | State: {d['status']}")
            print(f"[QRB] 🪐 Realm Bridge Linked | Level: {round(d['sync_level'] - 0.002,4)} | State: {d['status']}")
            print(f"[STABILIZER] 🧿 Field Stable | Level: {round(d['sync_level'] + 0.004,4)} ✅")
        else:
            heal()
            return
        time.sleep(9)
