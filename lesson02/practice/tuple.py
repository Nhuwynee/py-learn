student = ("Taro", 20, "Tokyo")
name, age, _ = student  # bỏ qua city

print(name, age)  # Taro 20

nums = (1, 2, 3, 4, 5)
first, *middle, last = nums

print(first) # 1
print(middle) # [2, 3, 4]
print(last) # 5

def get_min_max(numbers: list[float]) -> tuple[float, float]:
    minimum = min(numbers)
    maximum = max(numbers)
    return minimum, maximum  # Python tự gói thành tuple

scores = [7.5, 8.0, 6.5, 9.0, 8.5]
min_score, max_score = get_min_max(scores)

print("Min:", min_score)
print("Max:", max_score)

# dùng tuple làm key ghép nhiều thông tin (first_name, last_name)
students = {}

key1 = ("Nguyen", "An")
key2 = ("Tran", "Binh")

students[key1] = 8.5
students[key2] = 9.0

print(students[("Nguyen", "An")])  # 8.5

# duyệt tuple song song với zip()
a = (1, 2, 3)
b = ("A", "B", "C")

for x, y in zip(a, b):
    print(x, y)