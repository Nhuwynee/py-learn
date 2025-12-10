print("4.7 Thực hành nhanh về cấu trúc điều kiện")
print("1. =====================")
def print_age(age: int) -> str:
    if age < 0:
        print("Tuổi không thể âm")
    elif age < 11:
        print("Trẻ con")
    elif age < 17:
        print("Thiếu niên")
    elif age < 30:
        print("Thanh niên")
    else:
        print("Người già")

age = int(input("Nhập tuổi: "))
print_age(age)

print("2. =====================")
n = int(input("Nhập số nguyên dương: "))
if n < 0:
    print("Vui lòng nhập số nguyên dương")
else:
    result = "Even" if n % 2 == 0 else "Odd"
    print(result)

print("3. =====================")
year = int(input("Nhập năm: "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f"{year} là năm nhuận")
else:
    print(f"{year} không phải năm nhuận")