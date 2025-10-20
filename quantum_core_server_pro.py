import importlib
import threading
import time
import traceback

MODULES = [
    "quantum_genesis_engine",
    "quantum_field_stabilizer",
    "quantum_flux_regulator",
    ...
    "ascension_gate"
]

def run_module(name):
    try:
        mod = importlib.import_module(f"core.{name}")   # 🔹 Tự động import theo tên file trong thư mục /core/
        if hasattr(mod, "run_layer"):                   # 🔹 Kiểm tra xem file có hàm run_layer() không
            print(f"[🌀] Kích hoạt tầng: {name}")
            mod.run_layer()                             # 🔹 Nếu có thì gọi nó
        else:
            print(f"[⚠️] {name} không có run_layer(), bỏ qua.")
    except Exception as e:
        print(f"[❌] Lỗi khi chạy {name}: {e}")
        traceback.print_exc()
