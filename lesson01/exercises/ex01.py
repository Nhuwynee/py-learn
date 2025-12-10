print("Bài tập 1: Kiểm tra và tìm ngày kế tiếp, ngày trước đó")

def input_positive_number(prompt: str, min_value: int = None, max_value: int = None) -> int:
    value = input(prompt)

    while not (
        value.isdigit()
        and int(value) > 0
        and (min_value is None or int(value) >= min_value)
        and (max_value is None or int(value) <= max_value)
    ):
        print("Giá trị không hợp lệ!")
        value = input(prompt)

    return int(value)


def is_leap_year(year: int) -> bool:
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)


def days_in_month(month: int, year: int) -> int:
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    if month in (4, 6, 9, 11):
        return 30
    return 29 if is_leap_year(year) else 28


def get_next_date(day: int, month: int, year: int) -> tuple:
    day += 1
    if day > days_in_month(month, year):
        day = 1
        month += 1
        if month > 12:
            month = 1
            year += 1
    return day, month, year


def get_prev_date(day: int, month: int, year: int) -> tuple:
    day -= 1
    if day < 1:
        month -= 1
        if month < 1:
            month = 12
            year -= 1
        day = days_in_month(month, year)
    return day, month, year

year = input_positive_number("Nhập năm ( > 0 ): ", 1)
month = input_positive_number("Nhập tháng (1 – 12): ", 1, 12)

max_day = days_in_month(month, year)
day = input_positive_number("Nhập ngày: ", 1, 31)

while day > max_day:
    print(f"Ngày không hợp lệ! Tháng {month} năm {year} chỉ có {max_day} ngày")
    day = input_positive_number("Nhập ngày: ", 1, 31)

print(f"\nNgày nhập: {day}/{month}/{year}")

prev_day, prev_month, prev_year = get_prev_date(day, month, year)
next_day, next_month, next_year = get_next_date(day, month, year)

print(f"Ngày trước đó: {prev_day}/{prev_month}/{prev_year}")
print(f"Ngày kế tiếp : {next_day}/{next_month}/{next_year}")
