# core/__init__.py
import importlib, os

__all__ = []

for file in os.listdir(os.path.dirname(__file__)):
    if file.endswith(".py") and not file.startswith("__"):
        module_name = file[:-3]
        importlib.import_module(f"core.{module_name}")
        __all__.append(module_name)

print(f"[CORE] 🧩 Đã nạp {len(__all__)} tầng năng lượng: {__all__}", flush=True)

