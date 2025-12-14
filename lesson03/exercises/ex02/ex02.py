from lesson03.exercises.ex02.student import (
    load_students_from_file,
    calc_avg_score,
    find_top_student,
    filter_failed,
)

while True:
    filename = input("Nhập tên file điểm sinh viên:: ")
    students = load_students_from_file(filename)

    if students is not None:
        break

    print("Vui lòng nhập lại")

for student in students:
    print(student)

print("\nĐiểm trung bình lớp: ", calc_avg_score(students))
print("\nSinh viên điểm cao nhất:\n", find_top_student(students))
print("\nDanh sách sinh viên bị rớt:")
for failed_student in filter_failed(students):
    print(failed_student)
