print("7.5 Thực hành nhanh về chuỗi")

print("\n9. =====================")
name = "lƯU ngỌc yẾn NHư"
print(f'Chuẩn hóa "{name}" => {name.title()}')

print("\n10. =====================")
def is_palindrome_slicing(s: str) -> bool:
    return s == s[::-1]

print(f'"level" là chuỗi đối xứng? -> {is_palindrome_slicing("level")}')
print(f'"madam" là chuỗi đối xứng? -> {is_palindrome_slicing("madam")}')
print(f'"122 1" là chuỗi đối xứng? -> {is_palindrome_slicing("122 1")}')

print("\n11. =====================")
def count_vowels(s: str) -> int:
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for char in s.lower():
        if char in vowels:
            count += 1
    return count

print(f'Số lượng nguyên âm trong chuỗi "level" là: {count_vowels("level")}')
print(f'Số lượng nguyên âm trong chuỗi "hello world" là: {count_vowels("hello world")}')