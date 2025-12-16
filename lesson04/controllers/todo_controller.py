from fastapi import APIRouter, status, Query, Path
from typing import List

from lesson04.schemas.to_do import TodoCreate, TodoUpdate, TodoOut
from lesson04.services import todo_service

todo_router = APIRouter(prefix="/todos", tags=["Todos"])


@todo_router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    response_model=TodoOut,
    responses={409: {"description": "Todo title already exists"}},
)
def create_todo(todo: TodoCreate) -> TodoOut:
    return todo_service.create_todo(todo)


@todo_router.get(
    "",
    status_code=status.HTTP_200_OK,
    response_model=List[TodoOut],
)
def get_todos(
    done: bool | None = None,
    keyword: str | None = None,
    limit: int = Query(10, ge=1, le=20),
) -> List[TodoOut]:
    return todo_service.get_all_todos(done=done, keyword=keyword, limit=limit)


@todo_router.get(
    "/{todo_id}",
    status_code=status.HTTP_200_OK,
    response_model=TodoOut,
    responses={404: {"description": "Todo not found"}},
)
def get_todo_by_id(todo_id: int) -> TodoOut:
    return todo_service.get_todo_by_id(todo_id)


@todo_router.put(
    "/{todo_id}",
    status_code=status.HTTP_200_OK,
    response_model=TodoOut,
    responses={
        404: {"description": "Todo not found"},
        409: {"description": "Todo title already exists"},
    },
)
def update_todo_put(todo_id: int, todo: TodoCreate) -> TodoOut:
    return todo_service.update_todo_put(todo_id, todo)


@todo_router.patch(
    "/{todo_id}",
    status_code=status.HTTP_200_OK,
    response_model=TodoOut,
    responses={
        404: {"description": "Todo not found"},
        409: {"description": "Todo title already exists"},
    },
)
def update_todo_patch(todo_id: int, todo: TodoUpdate) -> TodoOut:
    return todo_service.update_todo_patch(todo_id, todo)


@todo_router.delete(
    "/{todo_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={404: {"description": "Todo not found"}},
)
def delete_todo(todo_id: int) -> None:
    return todo_service.delete_todo(todo_id)
