# ValueError: sai kiểu dữ liệu đầu vào
# ZeroDivisionError: chia cho 0
# FileNotFoundError: file không tồn tại
# TypeError: truyền sai kiểu tham số
# IndexError: truy cập index không tồn tại


# Cú pháp try / except
try:
    raw = input("Nhập một số nguyên: ")
    x = int(raw)
    y = 10 / x
    print(f"Kết quả 10 / {x} =", y)
except ValueError:
    print("Lỗi: Bạn phải nhập một số nguyên hợp lệ!")
except ZeroDivisionError:
    print("Lỗi: Không thể chia cho 0!")
except Exception as e:
    print("Lỗi không xác định:", e)


# Bắt nhiều lỗi trong cùng một except
try:
    x = int("abc")
except (ValueError, TypeError):
    print("Lỗi nhập liệu!")


# Khối else trong try/except (ít dùng)
try:
    y = int(input("Nhập số: "))
except ValueError:
    print("Bạn nhập sai!")
else:
    print("Bạn nhập:", y)


# Khối finally

# Đóng kết nối DB
# try:
#     conn = connect_to_db() # mở kết nối DB
#     result = conn.query("SELECT * FROM users")
#     print(result)
# except Exception as e:
#     print("Lỗi khi truy vấn:", e)
# finally:
#     print("Đóng kết nối DB…")
#     conn.close()
#
# # Reset trạng thái hệ thống
# state = "busy"
#
# try:
#     print("Đang chạy tác vụ quan trọng…")
#     # risky_task()
# except Exception:
#     print("Tác vụ lỗi!")
# finally:
#     state = "idle"
#     print("Trạng thái đã reset về:", state)


# Tự tạo exception bằng raise
# def divide(a, b):
#     if b == 0:
#         raise ValueError("b không được = 0")
#     return a / b
#
# try:
#     divide(5, 0)
# except ValueError as e:
#     print("Lỗi:", e)


# Áp dụng Exception vào File I/O
filename = input("Nhập tên file: ")

try:
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("File không tồn tại!")
except PermissionError:
    print("Bạn không có quyền đọc file này!")
except Exception as e:
    print("Lỗi khác:", e)

# 3.10 Thực hành Exception Handling
# BTTH1 – Bắt lỗi nhập số

n = 0
while n <= 0:
    try:
        number = int(input("Nhập số nguyên dương: "))
        if number <= 0:
            print("Nhập số nguyên dương > 0! Nhập lại!")
        else:
            print("Bạn nhập:", number)
            break
    except ValueError:
        print("Lỗi: Bạn phải nhập một số nguyên hợp lệ! Nhập lại!")
    except Exception as e:
        print("Lỗi không xác định:", e)

# BTTH2 – Tạo menu và xử lý lỗi lựa chọn
while True:
    try:
        num = int(input("Nhập số 1-3: "))
        if num < 1 or num > 3:
            print("Nhập sai! Nhập lại!")
            continue
        break
    except ValueError:
        print("Lỗi: Bạn phải nhập một số nguyên hợp lệ! Nhập lại!")
    except Exception as e:
        print("Lỗi không xác định:", e)

if num == 1:
    print("1. Xin chào")
elif num == 2:
    print("2. tính chỉ số BMI")
else:
    print("3. Thoát")
