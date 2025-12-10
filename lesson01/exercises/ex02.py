print("Bài tập 2: Tính tổng S = 1 + 1/3! + 1/5! + ... + 1/(2n−1)!")

def factorial(n: int) -> int:
    s = 1
    for i in range(1, n + 1):
        s *= i
    return s

def sum_factorial(n: int) -> float:
    s = 1
    for i in range(2, n + 1):
        s += 1 / factorial(2 * i - 1)
    return s

n = int(input("Nhập n: "))
print(f"Tổng = {sum_factorial(n)}")
