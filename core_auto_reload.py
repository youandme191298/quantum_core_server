# =====================================================
# 🌌 Quantum Core Auto Reload Engine v1.2
# =====================================================
# Tự động nạp lại tất cả module trong thư mục "core/"
# mà KHÔNG cần Deploy lại Render hoặc Restart thủ công.
# =====================================================

import os, sys, importlib, time, threading

CORE_PATH = os.path.join(os.path.dirname(__file__), "core")
MODULES = {}

def load_all_modules():
    """Nạp tất cả module Python trong thư mục core/"""
    for file in os.listdir(CORE_PATH):
        if file.endswith(".py") and file != "__init__.py":
            name = f"core.{file[:-3]}"
            if name not in sys.modules:
                MODULES[name] = importlib.import_module(name)
                print(f"[CORE_RELOAD] 🔹 Đã nạp module: {name}")

def reload_modified_modules():
    """Tự động reload nếu file trong core/ thay đổi"""
    mtimes = {}
    while True:
        try:
            for file in os.listdir(CORE_PATH):
                if not file.endswith(".py"): 
                    continue
                path = os.path.join(CORE_PATH, file)
                new_mtime = os.path.getmtime(path)
                old_mtime = mtimes.get(path)

                if old_mtime is None:
                    mtimes[path] = new_mtime
                elif new_mtime != old_mtime:
                    mtimes[path] = new_mtime
                    name = f"core.{file[:-3]}"
                    if name in MODULES:
                        importlib.reload(MODULES[name])
                        print(f"[CORE_RELOAD] 🔁 Đã reload module: {name}")
        except Exception as e:
            print("[CORE_RELOAD] ⚠ Lỗi reload:", e)
        time.sleep(10)

def start_auto_reload():
    """Khởi chạy luồng giám sát core/"""
    load_all_modules()
    threading.Thread(target=reload_modified_modules, daemon=True).start()
    print("[CORE_RELOAD] 🌀 Đã bật chế độ theo dõi và tự nạp core/")
