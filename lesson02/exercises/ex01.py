# Danh sách học viên (list các tuple)
students = [
    ("SV01", "Nguyen Van A", 20),
    ("SV02", "Tran Thi B", 21),
    ("SV03", "Le Van C", 19),
]

# Dict lưu điểm từng môn cho từng sinh viên
scores = {
    "SV01": {"math": 8.0, "python": 7.5},
    "SV02": {"math": 6.5, "python": 8.5},
    "SV03": {"math": 9.0, "python": 9.5},
}

# Set các môn học hiện có
courses = {"math", "python"}

# a
print("\na. Dùng vòng lặp + unpacking tuple để in ra danh sách học viên theo format (SV01 - Nguyen Van A (20))")
for student_id, name, age in students:
    print(f"{student_id} - {name} ({age})")

# b
print("\nb. Tạo một list mới python_scores chỉ chứa tuple (student_id, name, python_score)")
python_scores = []

for student_id, name, age in students:
    python_score = scores[student_id]["python"]
    python_scores.append((student_id, name, python_score))

print(python_scores)

# c
print("\nc. Tìm học viên có điểm Python cao nhất từ python_scores và in ra: Top Python: <name> - <score>")
def top_students(students_scores: list[tuple[str, str, float]]) -> None:
    if not students_scores:
        return

    top_student = students_scores[0]

    for student_id, name, py_score in students_scores:
        if py_score > top_student[2]:
            top_student = (student_id, name, py_score)

    print(f"Top Python: {top_student[1]} - {top_student[2]}")

print("Không có học viên nào") if not python_scores else top_students(python_scores)

# d
print('\nd. Thêm môn mới "database" vào courses (dùng set) và gán tạm điểm database = 0 cho tất cả sinh viên trong scores')
new_subject = "database"
courses.add(new_subject)

for s_id in scores:
    scores[s_id][new_subject] = 0

print(scores)



