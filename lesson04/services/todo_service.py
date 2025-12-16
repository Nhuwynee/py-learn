from fastapi import HTTPException

from lesson04.schemas.to_do import TodoOut, TodoCreate, TodoUpdate

_todos: list[dict] = []
_id_counter: int = 1


def _validate_title_unique(title: str, exclude_id: int | None = None):
    title = title.lower()
    for t in _todos:
        if t["title"].lower() == title and t["id"] != exclude_id:
            raise HTTPException(409, "Todo title already exists")


def _get_index_by_id(todo_id: int) -> int:
    for i, t in enumerate(_todos):
        if t["id"] == todo_id:
            return i

    raise HTTPException(404, detail="Not found")


def create_todo(todo: TodoCreate) -> TodoOut:
    global _id_counter

    _validate_title_unique(todo.title)

    new_todo = todo.model_dump()
    new_todo["id"] = _id_counter

    _todos.append(new_todo)
    _id_counter += 1

    return TodoOut(**new_todo)


def get_all_todos(
    done: bool | None = None,
    keyword: str | None = None,
    limit: int = 10,
) -> list[TodoOut]:
    result = _todos

    if done is not None:
        result = [t for t in result if t["done"] == done]

    if keyword:
        k = keyword.lower()
        result = [t for t in result if k in t["title"].lower()]

    return [TodoOut(**t) for t in result[:limit]]


def get_todo_by_id(todo_id: int) -> TodoOut:
    index = _get_index_by_id(todo_id)
    return TodoOut(**_todos[index])


def update_todo_put(todo_id: int, todo: TodoCreate) -> TodoOut:
    index = _get_index_by_id(todo_id)

    _validate_title_unique(todo.title, exclude_id=todo_id)

    update_data = todo.model_dump()
    update_data["id"] = todo_id
    _todos[index] = update_data

    return TodoOut(**update_data)


def update_todo_patch(todo_id: int, todo: TodoUpdate) -> TodoOut:
    index = _get_index_by_id(todo_id)
    current_todo = _todos[index]
    update_data = todo.model_dump(exclude_unset=True)

    if "title" in update_data:
        _validate_title_unique(update_data["title"], exclude_id=todo_id)

    current_todo.update(update_data)

    return TodoOut(**current_todo)


def delete_todo(todo_id: int) -> None:
    index = _get_index_by_id(todo_id)
    _todos.pop(index)
    return
