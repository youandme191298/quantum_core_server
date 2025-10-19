# ===============================================
# 🌍 AI_Thien_Dia_Nhan Server (Liên kết Quantum Core)
# -----------------------------------------------
# - Nhận dữ liệu qubit từ Quantum_Core_Server_PRO
# - Phân tích năng lượng Thiên–Địa–Nhân
# - Ghi log – phản hồi cộng hưởng
# ===============================================

from flask import Flask, jsonify
import requests, json, time, threading
from datetime import datetime

app = Flask(__name__)

# Địa chỉ máy chủ lõi lượng tử
CORE_URL = "https://quantum-core-server.onrender.com/ai/run_once"

# ===============================================
# ⚙️ Hàm xử lý năng lượng
# ===============================================
def analyze_energy(data):
    counts = data.get("counts", {})
    total = sum(counts.values())
    if total == 0:
        return {"heaven":0,"earth":0,"human":0}
    p0 = counts.get("000", 0)/total
    p1 = counts.get("111", 0)/total
    balance = round((p1 - p0) * 100, 2)
    return {
        "heaven": round(p1*100, 2),
        "earth": round(p0*100, 2),
        "human": balance
    }

# ===============================================
# 🌐 API CHÍNH
# ===============================================
@app.route("/")
def home():
    return jsonify({
        "status": "online",
        "message": "AI Thiên–Địa–Nhân Server đang hoạt động",
        "routes": ["/sync_once", "/auto/status"]
    })

@app.route("/sync_once")
def sync_once():
    try:
        res = requests.get(CORE_URL, timeout=20)
        core_data = res.json()
        energy = analyze_energy(core_data)
        record = {
            "timestamp": datetime.utcnow().isoformat()+"Z",
            "core": core_data,
            "energy": energy
        }
        with open("energy_log.json","a") as f:
            f.write(json.dumps(record)+"\n")
        return jsonify(record)
    except Exception as e:
        return jsonify({"status":"error","error":str(e)})

# ===============================================
# 🤖 AI MODE: TỰ ĐỒNG BỘ NĂNG LƯỢNG
# ===============================================
AUTO = {"running": False}

def auto_loop(interval=600):
    AUTO["running"]=True
    while AUTO["running"]:
        try:
            requests.get("http://127.0.0.1:8080/sync_once")
        except:
            pass
        time.sleep(interval)
    AUTO["running"]=False

@app.route("/auto/start")
def auto_start():
    if not AUTO["running"]:
        threading.Thread(target=auto_loop,daemon=True).start()
        return jsonify({"status":"started"})
    return jsonify({"status":"already_running"})

@app.route("/auto/stop")
def auto_stop():
    AUTO["running"]=False
    return jsonify({"status":"stopped"})

@app.route("/auto/status")
def auto_status():
    return jsonify(AUTO)

# ===============================================
# 🚀 CHẠY SERVER
# ===============================================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
