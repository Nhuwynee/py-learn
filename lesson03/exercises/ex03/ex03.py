from task import Task
from lesson03.exercises.ex03.task import load_tasks, save_tasks
from datetime import datetime

filename = "tasks.txt"
tasks = load_tasks(filename)


def view_tasks(tasks: list[Task]) -> None:
    if not tasks:
        print("Không có task nào")
    else:
        for task in tasks:
            print(task)


def view_overdue_tasks(tasks: list[Task]) -> None:
    now = datetime.now()
    overdue = [t for t in tasks if t.is_overdue(now)]
    view_tasks(overdue)


def add_task(tasks: list[Task], filename: str) -> None:
    description = input("Nhập mô tả task: ").strip()

    while True:
        due_date_str = input("Hạn (YYYY-MM-DD): ").strip()
        try:
            due_date = datetime.strptime(due_date_str, "%Y-%m-%d")
            break
        except ValueError:
            print("Ngày không hợp lệ, nhập theo YYYY-MM-DD")

    while True:
        status = input("Trạng thái (todo / done): ").strip().lower()
        if status in ("todo", "done"):
            break
        print("Status chỉ được là 'todo' hoặc 'done'")

    tasks.append(Task(description, due_date, status))
    save_tasks(filename, tasks)
    print("Thêm task thành công")


def input_number(prompt: str) -> int:
    while True:
        number_str = input(prompt).strip()

        if not number_str.isdigit():
            print("Phải nhập số nguyên dương")
            continue

        number = int(number_str)
        if number > 0:
            return number

        print("Phải nhập > 0")


def mark_task_done(tasks: list[Task]) -> None:
    list_todo_index = []

    print('Danh sách task "todo":')
    count = 0
    for i in range(len(tasks)):
        task = tasks[i]
        if task.status == "todo":
            print(f"{i + 1}. {task}")
            list_todo_index.append(i + 1)
            count += 1

    if count == 0:
        print('Không có task "todo" để đánh dấu')
        return

    while True:
        index = input_number("Nhập số thứ tự muốn đánh dấu task: ")

        if index not in list_todo_index:
            print('Chỉ có thể chọn số thứ tự ở danh sách (status: "todo")')
            continue

        break

    tasks[index - 1].status = "done"
    print(f"Đã đánh dấu task {index} là done")

    save_tasks(filename, tasks)


# Menu
while True:
    print("\n------ Menu -------")
    print("1. Xem tất cả task")
    print("2. Xem các task quá hạn")
    print("3. Thêm task mới")
    print("4. Đánh dấu task là done")
    print("5. Thoát")

    choice = input_number("Nhập lựa chọn: ")

    match choice:
        case 1:
            view_tasks(tasks)

        case 2:
            view_overdue_tasks(tasks)

        case 3:
            add_task(tasks, filename)

        case 4:
            mark_task_done(tasks)

        case 5:
            print("Thoát chương trình")
            break

        case _:
            print("Lựa chọn không hợp lệ")
