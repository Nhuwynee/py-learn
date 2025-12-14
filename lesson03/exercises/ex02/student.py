class Student:
    def __init__(self, name: str, age: int, score: float):
        self.name = name
        self.age = age
        self.score = score

    def is_passed(self) -> bool:
        if self.score >= 5:
            return True
        return False

    def __str__(self) -> str:
        return f"{self.name} ({self.age}) - Điểm: {self.score}"


def load_students_from_file(filename: str) -> list[Student] | None:
    students = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line_number, line in enumerate(f, start=1):
                line = line.strip()

                if not line:
                    continue

                name, age, score = line.split(",")

                try:
                    age = int(age)
                    score = float(score)
                except ValueError:
                    print(f"Dòng {line_number} sai dữ liệu, bỏ qua")
                    continue

                students.append(Student(name, age, score))

    except FileNotFoundError:
        print("File không tồn tại")
        return None
    except Exception as e:
        print("Có lỗi xảy ra:", e)
        return None

    return students


def calc_avg_score(students: list[Student]) -> float:
    total = 0

    for student in students:
        total += student.score

    return round(total / len(students), 2)


def find_top_student(students: list[Student]) -> Student | None:
    if not students:
        return None

    max_student = students[0]

    for student in students:
        if student.score > max_student.score:
            max_student = student

    return max_student


def filter_failed(students: list[Student]) -> list[Student]:
    failed_students = []

    for student in students:
        if not student.is_passed():
            failed_students.append(student)

    return failed_students
