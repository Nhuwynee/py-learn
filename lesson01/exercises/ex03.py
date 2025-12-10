print("Bài tập 3: Thao tác chuỗi")
def normalize_strings(t: str) -> str:
    t = t.strip().lower().rstrip(".")
    if not t:
        return "."
    words = t.split()
    return words[0].capitalize() + " " + " ".join(words[1:]) + "."

print(normalize_strings("Hello worlD,   this Is python.."))