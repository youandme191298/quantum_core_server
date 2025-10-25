"""
Quantum Core Loader v1.0.0
Tác giả: youandme191298
Chức năng: Tự động nạp toàn bộ 40 tầng năng lượng từ quantum_layer_map.json
và khởi tạo pipeline lượng tử theo đúng thứ tự định nghĩa.
"""

import os
import json
import importlib
import time
import traceback

# ==============================
# Cấu hình cơ bản
# ==============================
LAYER_MAP_PATH = os.path.join(os.path.dirname(__file__), "..", "quantum_layer_map.json")
CORE_PATH = os.path.dirname(__file__)
LOG_PATH = os.path.join(CORE_PATH, "logs")
os.makedirs(LOG_PATH, exist_ok=True)
LOG_FILE = os.path.join(LOG_PATH, "quantum_loader.log")


def log(message: str):
    """Ghi log ra console và file."""
    ts = time.strftime("[%Y-%m-%d %H:%M:%S]")
    text = f"{ts} {message}"
    print(text)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(text + "\n")


def load_json(file_path):
    """Đọc file JSON cấu hình."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Không tìm thấy file cấu hình: {file_path}")
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def import_layer(module_name, layer_name):
    """Thử nạp module và khởi tạo."""
    try:
        mod = importlib.import_module(f"core.{module_name}")
        if hasattr(mod, "init_layer"):
            mod.init_layer()
            log(f"✅ {layer_name} – Đã khởi tạo thành công (init_layer).")
        else:
            log(f"⚙️  {layer_name} – Nạp module thành công (không có init_layer).")
        return True
    except Exception as e:
        log(f"❌ Lỗi khi nạp {layer_name}: {e}")
        traceback_str = "".join(traceback.format_tb(e.__traceback__))
        log(traceback_str)
        return False


def run_loader():
    """Chạy quá trình nạp toàn bộ hệ tầng."""
    start_time = time.time()
    log("=" * 80)
    log("🚀 BẮT ĐẦU KHỞI TẠO QUANTUM CORE SERVER PIPELINE")
    log("=" * 80)

    data = load_json(LAYER_MAP_PATH)
    domains = data.get("domains", [])
    total_layers = 0
    success = 0
    failed = 0

    for domain in domains:
        log(f"\n🌐 [Domain] {domain['name']}: {domain['description']}")
        for layer in domain["layers"]:
            total_layers += 1
            module_name = layer["file"].replace(".py", "")
            layer_name = f"Tầng {layer['id']:02d} – {layer['name']}"
            log(f"🔹 Đang nạp {layer_name} ...")
            ok = import_layer(module_name, layer_name)
            if ok:
                success += 1
            else:
                failed += 1
            time.sleep(0.1)  # cho cảm giác “nạp năng lượng” :D

    elapsed = time.time() - start_time
    log("\n" + "=" * 80)
    log(f"🏁 HOÀN TẤT KHỞI TẠO PIPELINE – Tổng: {total_layers}, Thành công: {success}, Lỗi: {failed}")
    log(f"⏱️ Thời gian: {elapsed:.2f} giây")
    log("=" * 80)

    return {"total": total_layers, "success": success, "failed": failed, "time": elapsed}


if __name__ == "__main__":
    result = run_loader()
    if result["failed"] == 0:
        log("🌈 HỆ THỐNG QUANTUM CORE ĐÃ SẴN SÀNG HOẠT ĐỘNG.")
    else:
        log("⚠️ Một số tầng chưa nạp được, kiểm tra log chi tiết trong core/logs/quantum_loader.log")
