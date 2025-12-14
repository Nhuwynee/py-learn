from bean.student import Student
from bean.bank_account import BankAccount
from bean.person import Person
from bean.logger import Logger
from lesson03.practice.bean.staff import Staff

# -----------------------------------------------
# Student

s1 = Student("An", 20, 8.5)
print(s1.name) # An
print(s1.age) # 20
print(s1.score) # 8.5

s2 = Student("Binh", 21, 7.8)

s1.introduce() # Xin chào, mình là An, 20 tuổi.
print(s1.is_passed()) # True


# 5.5 Danh sách đối tượng: list[Student]
students = [
    Student("An", 20, 8.5),
    Student("Binh", 21, 6.0),
    Student("Chi", 19, 4.5),
]


for s in students:
    s.introduce()


# Tính điểm trung bình của lớp
def calc_avg_score(students):
    if not students:
        return 0
    total = 0
    for s in students:
        total += s.score
    return total / len(students)

avg = calc_avg_score(students)
print("Điểm trung bình lớp:", avg)


# Tìm sinh viên điểm cao nhất
def find_top_student(students: list[Student]) -> Student | None:
    if not students:
        return None
    top = students[0]
    for s in students[1:]:
        if s.score > top.score:
            top = s
    return top

empty_list = []
best = find_top_student(students)

if not best:
    print("Ko có data")
else:
    print("Top student:", best.name, best.score)


# -----------------------------------------------
# Bank Account
acc = BankAccount("An", 1000)
acc.deposit(500)
acc.withdraw(300)
print(acc.get_balance()) # 1200


# -----------------------------------------------
# Person
p = Person("An", 20, 1000)
print(p)


# -----------------------------------------------
# Logger

# Sử dụng
logger = Logger()
logger.log("Xin chao", "Python", 3)


# *kwargs
def show_info(**kwargs):
    print(kwargs)

show_info(name="An", age=20, score=8.5)

# 5.8.3 Kết hợp *args và *kwargs
def introduce(
        name: str,
        age: int,
        *skills,
        title: str = "N/A",
        level: str = "basic",
        **extra_info) -> None:
    print("Name:", name)
    print("Age:", age)
    print("Skills:", skills)
    print("Title:", title)
    print("Level:", level)
    print("Extra:", extra_info)


introduce(
    "An",
    20,
    "Python",
    "Java",
    title="Developer",
    level="Fresher",
    hobby="gaming",
    city="Tokyo"
)


# -----------------------------------------------
# Staff

staff = Staff("An", 20, hobby="gaming", city="DN")
print(staff.extra)


# getattr(obj, "tên_thuộc_tính", giá_trị_mặc_định)
print(getattr(staff, "name"))
print(getattr(staff, "extra"))


# Truyền default để xử lý khi thuộc tính không tồn tại:
print(getattr(staff, "salary", "Không có lương"))