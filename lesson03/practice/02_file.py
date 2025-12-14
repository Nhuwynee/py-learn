filename = "data.txt"
try:
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read())
except Exception as e:
    print("Có lỗi xảy ra khi đọc file:", e)