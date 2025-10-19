from flask import Flask, jsonify, request
from datetime import datetime
import random, math

app = Flask(__name__)

# ⚛️ Ba tầng năng lượng chính:
THIEN = {"frequency": 1.618, "stability": 0.99}
DIA = {"magnetism": 7.83, "flow": 0.95}
NHAN = {"consciousness": 0.88, "clarity": 0.93}

# ⚙️ Hợp nhất năng lượng lượng tử ba tầng
def quantum_sync():
    # Độ đồng pha năng lượng (dao động cộng hưởng)
    sync = round((THIEN["frequency"] * DIA["flow"] * NHAN["clarity"]) / 3.14159, 5)
    # Dao động lượng tử ngẫu nhiên
    fluct = random.uniform(-0.02, 0.02)
    unified = sync + fluct
    return max(0.0, round(unified, 5))

# 📡 API kiểm tra hợp nhất năng lượng
@app.route('/ai_thien_dia_nhan/sync', methods=['GET'])
def sync_energy():
    result = {
        "timestamp": datetime.utcnow().isoformat(),
        "sync_level": quantum_sync(),
        "THIEN": THIEN,
        "DIA": DIA,
        "NHAN": NHAN,
        "status": "harmonized"
    }
    return jsonify(result)

# 🌍 API hiệu chỉnh năng lượng bằng tay (POST)
@app.route('/ai_thien_dia_nhan/calibrate', methods=['POST'])
def calibrate():
    data = request.get_json(force=True)
    for layer, values in data.items():
        if layer in ["THIEN", "DIA", "NHAN"]:
            for key, val in values.items():
                if key in globals()[layer]:
                    globals()[layer][key] = float(val)
    return jsonify({"status": "updated", "current_sync": quantum_sync()})

# 🚀 Khởi chạy (nếu chạy riêng)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
