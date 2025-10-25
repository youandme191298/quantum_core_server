"""
Quantum Core Loader v3.0
-----------------------------------------
Tác giả: youandme191298

Chức năng:
- Tự động nạp 40 tầng lượng tử từ quantum_layer_map.json
- Hiển thị tiến trình (progress bar)
- Ghi log chi tiết từng tầng
- Đo thời gian nạp từng tầng
- Tự phục hồi tầng lỗi
- Sau khi hoàn tất: HỢP NHẤT THIÊN – ĐỊA – NHÂN
"""

import os
import json
import importlib
import time
import traceback
from datetime import datetime

# ==============================
# CẤU HÌNH CƠ BẢN
# ==============================
LAYER_MAP_PATH = os.path.join(os.path.dirname(__file__), "..", "quantum_layer_map.json")
CORE_PATH = os.path.dirname(__file__)
LOG_PATH = os.path.join(CORE_PATH, "logs")
os.makedirs(LOG_PATH, exist_ok=True)
LOG_FILE = os.path.join(LOG_PATH, "quantum_loader.log")


# ==============================
# HÀM HỖ TRỢ
# ==============================
def log(msg: str):
    """Ghi log ra console và file."""
    ts = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    text = f"{ts} {msg}"
    print(text)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(text + "\n")


def progress_bar(current, total, bar_length=40):
    """Hiển thị thanh tiến trình."""
    percent = current / total
    filled = int(bar_length * percent)
    bar = "█" * filled + "-" * (bar_length - filled)
    print(f"\r[{bar}] {percent * 100:6.2f}% ({current}/{total})", end="", flush=True)


def load_json(path):
    """Đọc file JSON."""
    if not os.path.exists(path):
        raise FileNotFoundError(f"Không tìm thấy file cấu hình: {path}")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def import_layer(module_name, layer_name):
    """Thử import module, chạy init nếu có."""
    start = time.time()
    try:
        mod = importlib.import_module(f"core.{module_name}")
        if hasattr(mod, "init_layer"):
            mod.init_layer()
            log(f"✅ {layer_name} – Khởi tạo thành công (init_layer).")
        else:
            log(f"⚙️  {layer_name} – Nạp module thành công (không có init_layer).")
        elapsed = time.time() - start
        return True, elapsed
    except Exception as e:
        elapsed = time.time() - start
        log(f"❌ Lỗi khi nạp {layer_name}: {e}")
        tb = "".join(traceback.format_tb(e.__traceback__))
        log(tb)
        return False, elapsed


# ==============================
# CHƯƠNG TRÌNH CHÍNH
# ==============================
def run_loader():
    """Khởi động toàn bộ hệ tầng lượng tử."""
    start_time = time.time()
    log("=" * 100)
    log("🚀 BẮT ĐẦU KHỞI TẠO QUANTUM CORE SERVER PIPELINE (v3.0)")
    log("=" * 100)

    data = load_json(LAYER_MAP_PATH)
    domains = data.get("domains", [])
    total_layers = sum(len(d["layers"]) for d in domains)
    success, failed = 0, 0
    failed_layers = []

    index = 0
    for domain in domains:
        log(f"\n🌐 [DOMAIN] {domain['name']}: {domain['description']}")
        for layer in domain["layers"]:
            index += 1
            progress_bar(index, total_layers)
            layer_name = f"Tầng {layer['id']:02d} – {layer['name']}"
            module_name = layer["file"].replace(".py", "")

            log(f"\n🔹 Đang nạp {layer_name} ...")
            ok, elapsed = import_layer(module_name, layer_name)
            if ok:
                success += 1
                log(f"⏱️  Thời gian: {elapsed:.2f}s")
            else:
                failed += 1
                failed_layers.append(layer_name)
            time.sleep(0.05)

    print()  # xuống dòng sau progress bar
    log("\n" + "=" * 100)
    log(f"🏁 HOÀN TẤT KHỞI TẠO PIPELINE – Tổng tầng: {total_layers}")
    log(f"   ✅ Thành công: {success}")
    log(f"   ❌ Lỗi: {failed}")
    log(f"   ⏱️  Tổng thời gian: {time.time() - start_time:.2f}s")
    log("=" * 100)

    # ============================================
    # GIAI ĐOẠN 2: HỢP NHẤT THIÊN – ĐỊA – NHÂN
    # ============================================
    try:
        log("\n🌗 BẮT ĐẦU QUÁ TRÌNH HỢP NHẤT THIÊN – ĐỊA – NHÂN ...")
        from core.layer_thien import get_cosmic_shift
        from core.layer_dia import stabilize_energies
        from core.layer_nhan import adapt_to_intent
        from core.quantum_core_server_core import synchronize_thien_dia_nhan

        thien = get_cosmic_shift()
        dia = stabilize_energies()
        nhan = adapt_to_intent()
        result = synchronize_thien_dia_nhan(thien, dia, nhan)
        log(f"🌌 Kết quả hợp nhất Thiên–Địa–Nhân: {result:.4f}")
    except Exception as e:
        log(f"⚠️ Lỗi khi hợp nhất Thiên–Địa–Nhân: {e}")

    # ============================================
    # GIAI ĐOẠN 3: KHÔI PHỤC TẦNG LỖI (NẾU CÓ)
    # ============================================
    if failed_layers:
        log("\n🩹 BẮT ĐẦU THỬ KHÔI PHỤC CÁC TẦNG LỖI ...")
        recovered = 0
        for name in failed_layers:
            try:
                module_name = name.split("–")[-1].strip().lower().replace(" ", "_")
                mod = importlib.import_module(f"core.{module_name}")
                if hasattr(mod, "init_layer"):
                    mod.init_layer()
                    recovered += 1
                    log(f"💫 Phục hồi thành công: {name}")
            except Exception as e:
                log(f"⚠️ Không thể phục hồi {name}: {e}")
        log(f"🔁 Hoàn tất khôi phục – {recovered}/{len(failed_layers)} tầng hồi phục được.")

    # ============================================
    # KẾT LUẬN HỆ THỐNG
    # ============================================
    log("\n" + "=" * 100)
    if failed == 0:
        log("🌈 HỆ THỐNG QUANTUM CORE ĐÃ SẴN SÀNG HOẠT ĐỘNG ỔN ĐỊNH.")
    else:
        log("⚠️ Một số tầng chưa khởi tạo được – xem log để xử lý chi tiết.")
    log("=" * 100)

    return {"total": total_layers, "success": success, "failed": failed, "time": time.time() - start_time}


# ==============================
# MAIN ENTRY
# ==============================
if __name__ == "__main__":
    run_loader()
