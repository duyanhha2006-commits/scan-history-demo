import os
import datetime

# Thư mục để lưu lịch sử quét
history_dir = "history"

# Tạo thư mục nếu chưa có
os.makedirs(history_dir, exist_ok=True)

# Giả lập kết quả quét (ví dụ nmap, virus scan, v.v.)
scan_result = """
Scan Report:
--------------
Target: 192.168.1.1
Port 22: open (ssh)
Port 80: open (http)
Port 443: open (https)
Scan completed successfully.
"""

# Tạo tên file theo thời gian hiện tại
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
file_name = f"scan_{timestamp}.txt"
file_path = os.path.join(history_dir, file_name)

# Ghi kết quả vào file
with open(file_path, "w") as f:
    f.write(scan_result)

print(f"✅ Kết quả quét đã được lưu vào: {file_path}")
add demo code
