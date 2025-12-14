from datetime import datetime


class Task:
    def __init__(self, description: str, due_date: datetime, status: str = "todo"):
        self.description = description
        self.due_date = due_date  # datetime
        self.status = status  # "todo" hoặc "done"

    # Trả về True nếu quá hạn và chưa done
    def is_overdue(self, now: datetime) -> bool:
        return self.due_date < now and self.status == "todo"

    def __str__(self) -> str:
        # Ví dụ: "[TODO] Học Python (Hạn: 2025-01-10)"
        return f"[{self.status}] {self.description} (Hạn: {self.due_date.strftime("%Y-%m-%d")})"


def load_tasks(filename: str) -> list[Task] | None:
    tasks = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line_number, line in enumerate(f, start=1):
                line = line.strip()

                if not line:
                    continue

                description, due_date, status = line.split(";")

                try:
                    due_date = datetime.strptime(due_date, "%Y-%m-%d")
                except ValueError:
                    print(f"Dòng {line_number} sai, bỏ qua")
                    continue

                status = status.strip().lower()
                if status not in ("todo", "done"):
                    status = "todo"

                tasks.append(Task(description, due_date, status))

    except FileNotFoundError:
        print("File không tồn tại")
        return None
    except Exception as e:
        print("Có lỗi xảy ra:", e)
        return None

    return tasks


def save_tasks(filename: str, tasks: list[Task]) -> None:
    try:
        with open(filename, "w", encoding="utf-8") as f:
            for task in tasks:
                line = f"{task.description};{task.due_date.strftime('%Y-%m-%d')};{task.status}\n"
                f.write(line)
    except FileNotFoundError:
        print("File không tồn tại")
        return None
    except Exception as e:
        print("Có lỗi xảy ra khi lưu file:", e)
        return None
