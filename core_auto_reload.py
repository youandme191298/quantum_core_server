# ==============================================
# 🔁 Quantum Core Auto-Reload Engine – v3.2
# ==============================================
# Chức năng:
#   - Theo dõi thư mục core/
#   - Tự động reload module khi có thay đổi
#   - Hoạt động nền liên tục, không làm gián đoạn hệ thống
# ==============================================

import importlib
import os
import sys
import threading
import time
import traceback

CORE_PATH = "core"
WATCH_INTERVAL = 2  # giây giữa mỗi lần kiểm tra thay đổi

# ==============================================
# 📦 Hàm reload 1 module cụ thể
# ==============================================

def reload_module(module_name):
    """Tự động reload 1 module trong core/ khi có thay đổi."""
    try:
        if module_name in sys.modules:
            importlib.reload(sys.modules[module_name])
            print(f"♻️  [CORE_RELOAD] Đã reload module: {module_name}")
        else:
            importlib.import_module(module_name)
            print(f"🆕 [CORE_RELOAD] Đã load module mới: {module_name}")
    except Exception as e:
        print(f"❌ [CORE_RELOAD] Lỗi khi reload {module_name}: {e}")
        traceback.print_exc()

# ==============================================
# 🧠 Theo dõi thay đổi file trong thư mục core/
# ==============================================

def watch_core_directory():
    """Theo dõi thay đổi trong thư mục core/"""
    print("👁️  [CORE_WATCHER] Đang theo dõi thư mục core/ để reload tự động...")
    file_timestamps = {}

    # Lưu thời gian sửa đổi ban đầu
    for filename in os.listdir(CORE_PATH):
        if filename.endswith(".py"):
            path = os.path.join(CORE_PATH, filename)
            file_timestamps[path] = os.path.getmtime(path)

    # Theo dõi liên tục
    while True:
        try:
            for filename in os.listdir(CORE_PATH):
                if not filename.endswith(".py"):
                    continue
                path = os.path.join(CORE_PATH, filename)
                new_time = os.path.getmtime(path)
                old_time = file_timestamps.get(path, None)

                if old_time is None:
                    file_timestamps[path] = new_time
                    continue

                # Nếu file thay đổi
                if new_time != old_time:
                    file_timestamps[path] = new_time
                    module_name = f"{CORE_PATH}.{filename[:-3]}"  # bỏ đuôi .py
                    print(f"🌀 [CORE_WATCHER] Phát hiện thay đổi trong {filename}, tiến hành reload...")
                    reload_module(module_name)
                    time.sleep(1.0)
        except Exception as e:
            print(f"⚠️ [CORE_WATCHER] Lỗi khi theo dõi core/: {e}")
            traceback.print_exc()

        time.sleep(WATCH_INTERVAL)

# ==============================================
# 🚀 Chạy trong luồng nền
# ==============================================

def start_auto_reload():
    """Khởi động auto-reload trong luồng nền"""
    watcher_thread = threading.Thread(target=watch_core_directory, daemon=True)
    watcher_thread.start()
    print("✅ [CORE_AUTO] Auto-reload engine đã được khởi động.\n")

# ==============================================
# 🏁 Chạy riêng file (test thủ công)
# ==============================================

if __name__ == "__main__":
    print("⚙️ Quantum Core Auto-Reload Engine đang khởi động...")
    start_auto_reload()
    while True:
        time.sleep(1)
