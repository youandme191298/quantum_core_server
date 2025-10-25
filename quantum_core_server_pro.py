# ============================================================
# ⚛️ QUANTUM CORE SERVER PRO – PHIÊN BẢN 3.3
# ------------------------------------------------------------
# Tích hợp tự động:
#  - Khởi động pipeline nạp tầng (hỗ trợ emoji)
#  - Auto reload năng lượng Thiên–Địa–Nhân
#  - KeepAlive gọi qua lại giữa 2 server Render (hoặc Replit)
#  - Flask API để các hệ thống ngoài (như Minecraft) kết nối
# ============================================================

import os
import sys
import time
import threading
from datetime import datetime
import requests

# ============================================================
# 🔧 HÀM TIỆN ÍCH CHUNG
# ============================================================

def quantum_log(msg):
    now = datetime.now().strftime("[%H:%M:%S]")
    print(f"{now} {msg}")
    sys.stdout.flush()

# ============================================================
# 🌐 NẠP CÁC MODULE CỐT LÕI
# ============================================================

try:
    from core.quantum_core_loader import run_loader, quantum_log
except Exception as e:
    quantum_log(f"❌ Không thể nạp quantum_core_loader: {e}")
    sys.exit(1)

# ============================================================
# 🧠 AUTO RELOAD – CHU TRÌNH DAO ĐỘNG NĂNG LƯỢNG
# ============================================================

def auto_reload(delay=30):
    """
    Tự động tái nạp pipeline năng lượng mỗi X giây.
    """
    quantum_log(f"♻️ Bắt đầu chu trình tự tái nạp năng lượng mỗi {delay} giây.")
    while True:
        try:
            loaded = run_loader()
            quantum_log(f"🌗 Chu trình hợp nhất Thiên–Địa–Nhân hoàn tất ({len(loaded)} tầng).")
        except Exception as e:
            quantum_log(f"⚠️ Lỗi chu trình reload: {e}")
        time.sleep(delay)

# ============================================================
# 🔁 KEEPALIVE – GIỮ SERVER ONLINE 24/24
# ============================================================

def keepalive_loop():
    """
    Gọi sang server đối tác để tránh Render ngủ.
    Đặt biến môi trường PARTNER_SERVER_URL trỏ đến /ping của server kia.
    """
    url = os.getenv("PARTNER_SERVER_URL")
    if not url:
        quantum_log("⚠️ Không phát hiện PARTNER_SERVER_URL – bỏ qua KeepAlive.")
        return

    def loop():
        while True:
            try:
                r = requests.get(url, timeout=10)
                quantum_log(f"🔁 Ping sang {url} → {r.status_code}")
            except Exception as e:
                quantum_log(f"⚠️ Lỗi KeepAlive: {e}")
            time.sleep(150)

    threading.Thread(target=loop, daemon=True).start()

# ============================================================
# 🌐 FLASK API – CỔNG GIAO TIẾP NĂNG LƯỢNG NGOÀI
# ============================================================

from flask import Flask, jsonify

app = Flask(__name__)

# Giả lập các năng lượng đơn giản cho API
import random
def get_energy_value(scale=4.0, var=0.15):
    return round(random.uniform(scale - var, scale + var), 4)

@app.get("/energy/merge")
def get_energy_merge():
    thien = get_energy_value()
    dia = get_energy_value()
    nhan = get_energy_value()
    merged = round((thien + dia + nhan) / 3, 4)
    return jsonify({
        "thien": thien,
        "dia": dia,
        "nhan": nhan,
        "merged": merged,
        "timestamp": datetime.utcnow().isoformat()
    })

@app.get("/ping")
def ping():
    return jsonify({"status": "ok", "time": datetime.utcnow().isoformat()})

def run_api():
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)

# ============================================================
# 🚀 KHỞI ĐỘNG TOÀN HỆ THỐNG
# ============================================================

if __name__ == "__main__":
    quantum_log("=" * 80)
    quantum_log("🚀 KHỞI ĐỘNG QUANTUM CORE SERVER PRO – phiên bản 3.3")
    quantum_log("=" * 80)
    quantum_log(f"🧩 Python {sys.version.split()[0]} | OS: {os.uname().sysname}")

    # Khởi tạo hệ thống ban đầu
    loaded_layers = run_loader()
    quantum_log(f"✅ Đã khởi động {len(loaded_layers)} tầng năng lượng đầu tiên.")

    # Khởi động Flask API (song song)
    quantum_log("🌐 Mở cổng API Quantum tại /energy/merge & /ping ...")
    threading.Thread(target=run_api, daemon=True).start()

    # Kích hoạt KeepAlive song song
    keepalive_loop()

    # Bắt đầu chu trình tự reload mỗi 60 giây
    threading.Thread(target=auto_reload, args=(60,), daemon=True).start()

    # Giữ tiến trình sống liên tục
    while True:
        time.sleep(3600)
