def read_file_content(filename: str) -> str | None:
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print("File không tồn tại")
        return None
    except Exception as e:
        print("Có lỗi xảy ra:", e)
        return None


def count_word_frequency(text: str) -> dict[str, int]:
    words = text.split()
    word_frequency = {}

    for word in words:
        word_frequency[word] = word_frequency.get(word, 0) + 1

    return word_frequency


def count_words_in_file(text: str) -> int:
    return len(text.split())


def normalize_file_content(content: str) -> str:
    for char in ".,;:?!()[]":
        content = content.replace(char, "")
    return content.lower()


def get_top_10_words_in_file(text: str) -> list[tuple[str, int]]:
    word_frequency = count_word_frequency(text)

    word_list = []
    for word in word_frequency:
        word_list.append((word_frequency[word], word))

    word_list.sort(reverse=True)

    result = []
    for count, word in word_list[:10]:
        result.append((word, count))

    return result
