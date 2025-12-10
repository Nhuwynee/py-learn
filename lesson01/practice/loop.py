for i in range(5, 10):
    print(i, end='')
print()

names = ["Lưu", "Ngọc", "Yến", "Như"]
for name in names:
    print(name, end=' ')
print()

string = 'hello'
for char in string:
    print(char, end=' ')
print()

n = 5
while n > 0:
    print(n, end="\t")
    n -= 1
print()

# while True
# while True:
#     pwd = input("Nhập mật khẩu: ")
#     if pwd == "Abc123@":
#         print("Đúng rồi người đẹp")
#         break # bắt buộc luôn có break/return trong while True
#     print("Sai rồi! Chịu khó nhập lại đi em iu")

print()

row = 5
col = 6
for i in range(row):
    for j in range(col):
        print("*", end=' ')
    print()

print("\n5.6 Thực hành nhanh về cấu trúc lặp")
print("4. =====================")
age = int(input("Nhập tuổi (> 0): "))
while age <= 0:
    print("Tuổi phải lớn hơn 0. Nhập lại.")
    age = int(input("Nhập tuổi (> 0): "))

sum_age = 0
for age in range(1, age + 1):
    sum_age += age
print(f"Tổng từ 1 đến {age} = {sum_age}")

print("\n5. =====================")
sum_text = 0
text = input('Nhập 1 chuỗi bất kì: ')
for char in text:
    if char == 'a':
        sum_text += 1
print('Số lần ký tự a xuất hiện: ', sum_text)

print("\n6a. =====================")
for i in range(row):
    for j in range(col):
        if i == 0 or i == row - 1 or j == 0 or j == col - 1:
            print("*", end=' ')
        else:
            print(" ", end=' ')
    print()

print("\n6b. =====================")
for i in range(row + 1):
    for j in range(i):
        print("*", end=' ')
    print()





