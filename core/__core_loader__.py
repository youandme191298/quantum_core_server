# =====================================================
# 🧩 Quantum Core Loader v1.3
# =====================================================
# Quét, nạp và khởi động toàn bộ tần năng lượng trong thư mục core/
# =====================================================

import importlib, os, threading, time

def load_all_layers():
    core_path = os.path.dirname(__file__)
    loaded_modules = set()

    print("\n[CORE_LOADER] 🧩 Đang quét các tần năng lượng trong core/...")

    while True:
        for file in os.listdir(core_path):
            if file.endswith(".py") and not file.startswith("__"):
                module_name = f"core.{file[:-3]}"
                if module_name not in loaded_modules:
                    try:
                        module = importlib.import_module(module_name)
                        if hasattr(module, "run_layer"):
                            threading.Thread(target=module.run_layer, daemon=True).start()
                            print(f"[CORE_LOADER] ⚙️ Đã kích hoạt tần: {module_name}")
                            loaded_modules.add(module_name)
                    except Exception as e:
                        print(f"[CORE_LOADER] ⚠️ Lỗi khi tải {module_name}: {e}")
        time.sleep(10)
