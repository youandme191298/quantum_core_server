import os
import importlib
import threading
import time
import traceback
from datetime import datetime

# =========================
#  QUANTUM CORE SERVER PRO
# =========================
# Tự động nhận diện – tải tầng năng lượng – chạy song song – giám sát tình trạng 24/24
# Phiên bản: v3.1 | Cập nhật: 20-10-2025
# =========================

CORE_PATH = "core"
SCAN_INTERVAL = 180        # Thời gian quét lại thư mục core (giây)
THREAD_DELAY = 0.8         # Khoảng cách giữa mỗi tầng khi khởi động
MONITOR_INTERVAL = 300     # Giám sát trạng thái mỗi 5 phút

active_threads = {}        # Theo dõi trạng thái tầng
lock = threading.Lock()


# === TỰ ĐỘNG QUÉT DANH SÁCH FILE TRONG /core/ ===
def scan_modules():
    modules = []
    for file in os.listdir(CORE_PATH):
        if file.endswith(".py") and not file.startswith("__"):
            modules.append(file[:-3])  # bỏ phần .py
    return sorted(modules)


# === CHẠY MỘT TẦNG ===
def run_module(name):
    global active_threads
    try:
        mod = importlib.import_module(f"{CORE_PATH}.{name}")
        if hasattr(mod, "run_layer"):
            print(f"🌀 [Kích hoạt] {name}")
            mod.run_layer()
        else:
            print(f"⚠️ [Bỏ qua] {name} không có hàm run_layer()")
    except Exception as e:
        print(f"❌ [Lỗi] {name}: {e}")
        traceback.print_exc()
    finally:
        with lock:
            active_threads[name] = False


# === KHỞI ĐỘNG TẤT CẢ TẦNG ===
def start_all_layers():
    print("\n🚀 Bắt đầu khởi động toàn bộ tầng năng lượng...")
    modules = scan_modules()
    with lock:
        for name in modules:
            if name not in active_threads or not active_threads[name]:
                t = threading.Thread(target=run_module, args=(name,), daemon=True)
                t.start()
                active_threads[name] = True
                time.sleep(THREAD_DELAY)
    print("🌍 Tất cả tầng đã được kích hoạt.")


# === TỰ ĐỘNG GIÁM SÁT – KHỞI ĐỘNG LẠI NẾU TẦNG DỪNG ===
def monitor_layers():
    while True:
        time.sleep(MONITOR_INTERVAL)
        with lock:
            total = len(active_threads)
            active = sum(active_threads.values())
        print(f"[MONITOR] {datetime.now().strftime('%H:%M:%S')} → Hoạt động: {active}/{total} tầng.")
        if active < total:
            print("⚙️ Một số tầng đã ngừng. Tiến hành khởi động lại...")
            start_all_layers()


# === QUÉT TỰ ĐỘNG NẾU THÊM TẦNG MỚI VÀ KHỞI ĐỘNG NGAY ===
def auto_reload_core():
    known = set(scan_modules())
    while True:
        time.sleep(SCAN_INTERVAL)
        current = set(scan_modules())
        new_modules = current - known
        if new_modules:
            print(f"\n🔁 Phát hiện tầng mới: {', '.join(new_modules)} – Tự động tải thêm.")
            with lock:
                for name in new_modules:
                    if name not in active_threads:
                        t = threading.Thread(target=run_module, args=(name,), daemon=True)
                        t.start()
                        active_threads[name] = True
                        time.sleep(THREAD_DELAY)
            known = current


# === HÀM MAIN KHỞI ĐỘNG TOÀN HỆ THỐNG ===
def main():
    print("""
╔════════════════════════════════════════════════════╗
║   ⚙️ Quantum Core Server Pro v3.1                  ║
║   Trạng thái: Hoạt động 24/24 – Auto Discovery     ║
║   Năng lượng: Thiên – Địa – Nhân – Đạo – Vô Cực   ║
╚════════════════════════════════════════════════════╝
""")

    start_all_layers()

    threading.Thread(target=auto_reload_core, daemon=True).start()
    threading.Thread(target=monitor_layers, daemon=True).start()

    while True:
        time.sleep(60)


# === CHẠY HỆ THỐNG ===
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n🧘 Hệ thống dừng thủ công.")
    except Exception as e:
        print(f"❌ Lỗi hệ thống: {e}")
        traceback.print_exc()
