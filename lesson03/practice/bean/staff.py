class Staff:
    def __init__(self, name: str, age: int, **kwargs):
        self.name = name
        self.age = age
        self.extra = kwargs

# Nơi dùng
staff = Staff("An", 20, hobby="gaming", city="DN")
print(staff.extra)