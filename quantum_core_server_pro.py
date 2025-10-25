"""
Quantum Core Server Pro – Main Entry Point
-------------------------------------------
Tác giả: youandme191298

Chức năng:
- Khởi tạo toàn bộ pipeline lượng tử thông qua quantum_core_loader.py
- Tự kiểm tra môi trường Python và gói phụ thuộc
- Ghi log tiến trình khởi động
- Hỗ trợ reload nhanh và phục hồi khi pipeline gián đoạn
"""

import os
import sys
import time
import platform
from datetime import datetime

# ===========================
# CẤU HÌNH CƠ BẢN
# ===========================
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
CORE_PATH = os.path.join(ROOT_PATH, "core")
LOG_PATH = os.path.join(CORE_PATH, "logs")
os.makedirs(LOG_PATH, exist_ok=True)
LOG_FILE = os.path.join(LOG_PATH, "quantum_server_startup.log")


def log(msg: str):
    """Ghi log khởi động hệ thống."""
    ts = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    text = f"{ts} {msg}"
    print(text)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(text + "\n")


# ===========================
# KIỂM TRA MÔI TRƯỜNG
# ===========================
def check_environment():
    log("🔍 Đang kiểm tra môi trường hệ thống ...")
    python_ver = sys.version.split()[0]
    os_info = platform.platform()
    log(f"🧠 Python version: {python_ver}")
    log(f"💻 Hệ điều hành: {os_info}")

    required_version = (3, 8)
    if sys.version_info < required_version:
        log("⚠️ Phiên bản Python quá thấp. Cần >= 3.8")
        sys.exit(1)

    try:
        import importlib, json
        log("✅ Các thư viện cơ bản đã sẵn sàng.")
    except ImportError as e:
        log(f"❌ Thiếu thư viện cần thiết: {e}")
        sys.exit(1)


# ===========================
# KHỞI TẠO PIPELINE LƯỢNG TỬ
# ===========================
def start_quantum_pipeline():
    """Chạy hệ thống lượng tử qua loader."""
    from core.quantum_core_loader import run_loader

    log("\n⚙️  ĐANG KHỞI ĐỘNG QUANTUM CORE SERVER ...")
    start = time.time()
    result = run_loader()
    duration = time.time() - start

    log("\n" + "=" * 90)
    log(f"🪐 KẾT THÚC QUÁ TRÌNH KHỞI TẠO QUANTUM CORE SERVER")
    log(f"   ⏱️  Thời gian tổng: {duration:.2f}s")
    log("=" * 90)

    # Hiển thị kết quả tóm tắt
    total, success, failed = result["total"], result["success"], result["failed"]
    log(f"📊 TỔNG TẦNG: {total}, THÀNH CÔNG: {success}, LỖI: {failed}")
    if failed == 0:
        log("🌈 TOÀN BỘ HỆ THỐNG QUANTUM CORE ĐÃ SẴN SÀNG HOẠT ĐỘNG.")
    else:
        log("⚠️ MỘT SỐ TẦNG CHƯA NẠP ĐƯỢC – KIỂM TRA LOG CHI TIẾT.")


# ===========================
# CHẾ ĐỘ RELOAD NHANH
# ===========================
def auto_reload(delay=10):
    """Tự động reload pipeline mỗi X giây (tùy chọn)."""
    log(f"🔁 Kích hoạt chế độ auto-reload mỗi {delay}s (bấm Ctrl+C để dừng).")
    try:
        while True:
            start_quantum_pipeline()
            log(f"🌀 Chờ {delay}s trước khi reload lại pipeline ...")
            time.sleep(delay)
    except KeyboardInterrupt:
        log("🧘‍♂️ Auto-reload dừng theo yêu cầu người dùng.")


# ===========================
# MAIN ENTRY
# ===========================
if __name__ == "__main__":
    log("=" * 90)
    log("🚀 KHỞI ĐỘNG QUANTUM CORE SERVER PRO – phiên bản 2.0")
    log("=" * 90)
    check_environment()

    # Chạy hệ thống chính
    start_quantum_pipeline()

    # Nếu bạn muốn auto reload liên tục, bật dòng dưới:
    # auto_reload(delay=30)
