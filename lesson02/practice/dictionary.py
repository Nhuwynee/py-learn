from typing import Any

empty_dict = {}

student = {
    "name": "Nguyen Van A",
    "age": 20
}

user = dict(name="An", age=25)
print(user)  # {'name': 'An', 'age': 25}

# Từ list/tuple các cặp 2 phần tử
pairs = [("a", 1), ("b", 2), ("c", 3)]
my_dict = dict(pairs)
print(my_dict)  # {'a': 1, 'b': 2, 'c': 3}

student2 = {"name": "An", "age": 20}
print(student2["name"])  # An

# print(student2["address"])  # KeyError: 'address'

print(student2.get("name")) # An
print(student2.get("address")) # None

# Fallback trả giá trị mặc định
user = dict(name="An", age=25)
print(user.get("email", "N/A")) # nếu thiếu, mặc định là N/A
print(user.get("active", False))

# them mới / cập nhật
student2["age"] = 21 # cập nhật
student2["address"] = "Hanoi" # thêm mới

print(student2) # {'name': 'An', 'age': 21, 'address': 'Hanoi'}

# BTTH7
student_7: dict[str, Any] = {
    "name": "Nguyen Van A",
    "age": 20,
    "scores": [7.5, 8.0, 6.5, 9.0],
}

# a
print("name", ":", student_7["name"])
print("age", ":", student_7["age"])

# b
student_7["avg_score"] = sum(student_7["scores"]) / len(student_7["scores"])
print(student_7)

# BTTH8
s = "hello world"
counter = {}
for c in s:
    counter[c] = counter.get(c, 0) + 1

