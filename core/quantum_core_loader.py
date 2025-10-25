# ============================================================
# 🌐 QUANTUM CORE LOADER v3.2 – Hỗ trợ emoji & ký tự đặc biệt
# ------------------------------------------------------------
# Tác giả: youandme191298
# Mục đích:
#  - Tự động nạp tất cả tầng năng lượng từ quantum_layer_map.json
#  - Hỗ trợ file có emoji hoặc ký tự đặc biệt trong tên (☯, 🔮, 💠, 🌈, v.v.)
#  - Log quá trình nạp tầng rõ ràng & ổn định trên Render Cloud
# ============================================================

import os
import sys
import json
import importlib.util
from datetime import datetime

# ------------------------------------------------------------
# 🧩 Hàm log định dạng chuẩn
# ------------------------------------------------------------
def quantum_log(message):
    time_str = datetime.now().strftime("[%H:%M:%S]")
    print(f"{time_str} {message}")
    sys.stdout.flush()

# ------------------------------------------------------------
# ⚙️ Hàm nạp module từ đường dẫn (hỗ trợ emoji)
# ------------------------------------------------------------
def load_module_from_path(module_path):
    """
    Nạp module từ đường dẫn file thực tế.
    Cho phép emoji, dấu cách, ký tự đặc biệt trong tên file.
    """
    try:
        module_name = os.path.splitext(os.path.basename(module_path))[0]
        spec = importlib.util.spec_from_file_location(module_name, module_path)
        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)
        quantum_log(f"✅ Đã nạp: {os.path.basename(module_path)}")
        return module
    except Exception as e:
        quantum_log(f"❌ Lỗi khi nạp {module_path}: {e}")
        return None

# ------------------------------------------------------------
# 🔍 Hàm nạp bản đồ tầng lượng tử (quantum_layer_map.json)
# ------------------------------------------------------------
def load_layer_map():
    layer_map_path = os.path.join(os.path.dirname(__file__), "..", "quantum_layer_map.json")
    try:
        with open(layer_map_path, "r", encoding="utf-8") as f:
            layers = json.load(f)
        quantum_log(f"📜 Đã đọc {len(layers)} tầng năng lượng từ quantum_layer_map.json")
        return layers
    except Exception as e:
        quantum_log(f"⚠️ Không thể đọc quantum_layer_map.json: {e}")
        return []

# ------------------------------------------------------------
# 🚀 Hàm khởi động pipeline nạp tầng
# ------------------------------------------------------------
def run_loader():
    """
    Nạp lần lượt các tầng trong quantum_layer_map.json
    theo đúng thứ tự id, hỗ trợ icon emoji trong tên file.
    """
    base_dir = os.path.dirname(__file__)
    layers = load_layer_map()
    loaded_layers = []

    if not layers:
        quantum_log("⚠️ Không tìm thấy tầng năng lượng nào để nạp.")
        return []

    for layer in sorted(layers, key=lambda x: x.get("id", 0)):
        try:
            name = layer.get("name", "Không rõ")
            file_name = layer.get("file")
            if not file_name:
                quantum_log(f"⚠️ Bỏ qua tầng {name} (không có file).")
                continue

            module_path = os.path.join(base_dir, file_name)
            quantum_log(f"🔹 Đang nạp {name} ...")

            module = load_module_from_path(module_path)
            if module:
                init_func = getattr(module, "init_layer", None)
                if callable(init_func):
                    init_func()
                    quantum_log(f"✨ {name}: Khởi tạo thành công.")
                loaded_layers.append(name)
        except Exception as e:
            quantum_log(f"❌ Lỗi tại tầng {name}: {e}")

    quantum_log("🌈 Tất cả tầng khả dụng đã được nạp hoàn tất.")
    return loaded_layers

# ------------------------------------------------------------
# 🧪 Chạy thử nếu thực thi độc lập
# ------------------------------------------------------------
if __name__ == "__main__":
    quantum_log("🌀 KIỂM TRA KHỞI ĐỘNG QUANTUM CORE LOADER ...")
    run_loader()
