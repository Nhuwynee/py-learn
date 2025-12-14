from datetime import datetime

now = datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

# Thứ tự tham số: year, month, day, hour, minute, second
specific = datetime(2025, 1, 1, 8, 30, 0)
print(specific)

# Các ký hiệu format phổ biến
# Ký hiệu	Ý nghĩa
# %Y	    Năm (4 chữ số)
# %m	    Tháng (01–12)
# %d	    Ngày
# %H	    Giờ (00–23)
# %M	    Phút
# %S	    Giây
# %A	    Tên thứ (Monday, Tuesday ...)

print(now.strftime("Hôm nay là %A, ngày %d/%m/%Y"))

# Chuyển chuỗi thành datetime: strptime
s = "2025-02-14 20:30:00"
dt = datetime.strptime(s, "%Y-%m-%d %H:%M:%S")
print(dt)


# 4.8 Đo thời gian thực thi đoạn code

import time

start = time.time()

# --- đoạn code cần đo thời gian ---
result = 0
for i in range(1_000_000):
    result += i
# ----------------------------------

end = time.time()
elapsed = end - start
print("Thời gian thực thi:", elapsed, "giây")

# Dùng perf_counter() (chính xác hơn)
from time import perf_counter

start = perf_counter()
result = 0
for i in range(1_000_000):
    result += i
end = perf_counter()

print("Elapsed:", end - start)