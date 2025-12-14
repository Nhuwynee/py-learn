from lesson03.exercises.ex01.utils.file_utils import (
    count_word_frequency,
    read_file_content,
    count_words_in_file,
    normalize_file_content,
    get_top_10_words_in_file,
)

# 1
print("\n1. Chương trình hỏi người dùng")
while True:
    filename = input("Nhập tên file cần phân tích: ")
    content = read_file_content(filename)

    if content is not None:
        break

    print("Vui lòng nhập lại")


content = read_file_content(filename)
normalize_content = normalize_file_content(content)

# 2
print("\n2. Đọc toàn bộ nội dung file, chuẩn hóa")
print("-> ", normalize_content)

# 3
print("\n3. Tách từ theo dấu cách, đếm số lần xuất hiện của từng từ")
print("-> ", count_word_frequency(normalize_content))

# 4
print("\n4. In ra: ")
print(f"-> Tổng số từ: {count_words_in_file(normalize_content)}")

print("\n-> Top 10 từ xuất hiện nhiều nhất:")
top_10_words = get_top_10_words_in_file(normalize_content)
for word, count in top_10_words:
    print(f"- {word}: {count}")
