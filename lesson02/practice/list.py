from xmlrpc.client import MAXINT, MININT

numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", True, 3.14]
empty = []

print(numbers)
print(mixed)
print(empty)

numbers = [10, 20, 30, 40, 50]

print(numbers[1:4]) # [20, 30, 40]
print(numbers[:3]) # [10, 20, 30]
print(numbers[2:]) # [30, 40, 50]
print(numbers[:]) # copy list, tham chiếu qua địa chỉ mới
print(numbers[::2]) # [10, 30, 50] => bỏ qua 1 phần tử
print(numbers[::-1]) # đảo list

numbers.append(100)
numbers.insert(2, 200)
print(numbers)

nums = [4, 7, 1, 9]

print(len(nums)) # số phần tử
print(sum(nums)) # tổng
print(sorted(nums)) # trả về list mới đã sort

print(nums)

nums.sort(reverse=False)
print(nums)

# Duyệt index + value bằng enumerate() (vừa lấy index, vừa value)
for i, value in enumerate(nums, start=1):
    print(i, value)

# Duyệt song song nhiều list bằng zip()
students = ["A", "B", "C", "D"]
math = [9.0, 7.5, 8.0]
english = [8.5, 6.0, 9.0]

for s, m, e in zip(students, math, english):
    print(s, m, e)
# Lưu ý: zip() sẽ dừng khi list ngắn nhất kết thúc

# List comprehension
nums2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Cách truyền thống
new_list = []
for n in nums2:
    new_list.append(n + 1)
print(new_list)

# Tăng mỗi số lên 1
new_list = [n + 1 for n in nums2]
print(new_list)

# Lọc phần tử theo điều kiện
evens = [x for x in nums2 if x % 2 == 0]
print(evens) # [0, 2, 4, 6, 8]

# Nested list comprehension
pairs = [(x, y) for x in [1, 2] for y in [3, 4]]
print(pairs) # [(1, 3), (1, 4), (2, 3), (2, 4)]

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

print(matrix[1][2]) # 6

# Duyệt 2 chiều
for row in matrix:
    for value in row:
        print(value, end=" ")
    print()

a = [1, 2, 3]
# b = a
# Copy đúng cách
# b = a.copy()
b = a[:]
b[0] = 100
print(a)

# BTTH1
scores = [7.5, 8.0, 6.5, 9.0, 8.5]
avg = sum(scores) / len(scores)
print(avg)

avg2 = 0
sum = 0
for score in scores:
    sum += score
avg2 = sum / len(scores)
print(avg2)

print(max(scores))

max_score = MININT
for score in scores:
    if score > max_score:
        max_score = score
print(max_score)

print(min(scores))

min_score = MAXINT
for score in scores:
    if score < min_score:
        min_score = score
print(min_score)

# BTTH2
nums_2 = [5, -2, 8, -1, 0, 3, -10]
result_2 = []
for n in nums_2:
    if n >= 0:
        result_2.append(n)
print(f"Xóa số âm khỏi list: {result_2}")

#BTTH3
# C1
pairs = [[1,2,3],[4,5],[6]]
result = []
for pair in pairs:
    for pair2 in pair:
        result.append(pair2)
print(result)

# C2
flat = [x for sub in result for x in sub]
print(flat)


