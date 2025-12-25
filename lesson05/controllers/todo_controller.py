from http import HTTPStatus
from typing import Optional

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from starlette.responses import Response

from dependencies.db import get_db
from schemas.request.todo_schema import TodoCreate, TodoUpdate, TodoFilter
from schemas.response.todo_out_schema import TodoOut
from schemas.response.error_response import ErrorSchema
from services.todo_service import TodoService

todo_router = APIRouter(prefix="/todos", tags=["Todo Controller"])

@todo_router.post(
    "/",
    response_model=TodoOut,
    status_code=HTTPStatus.CREATED,
    responses={
        409: {"model": ErrorSchema, "description": "Todo title already exists"},
        422: {"model": ErrorSchema, "description": "Validation Error"},
    },
)
async def create_todo(
    request: TodoCreate, db: Session = Depends(get_db)
) -> TodoOut:
    todo = TodoService(db).create_todo(request)
    return todo


@todo_router.get(
    "/{todo_id}",
    response_model=TodoOut,
    status_code=HTTPStatus.OK,
    responses={
        404: {"model": ErrorSchema, "description": "Todo not found"},
        422: {"model": ErrorSchema, "description": "Validation Error"},
    },
)
async def get_todo(todo_id: int, db: Session = Depends(get_db)) -> TodoOut:
    todo = TodoService(db).get_todo(todo_id)
    return todo


@todo_router.get(
    "/",
    response_model=list[TodoOut],
    status_code=HTTPStatus.OK,
    responses={
        422: {"model": ErrorSchema, "description": "Validation Error"},
    },
)
async def list_todos(
    db: Session = Depends(get_db), filters: TodoFilter = Depends()
) -> list[TodoOut]:
    todos = TodoService(db).list_todos(filters)
    return todos


@todo_router.put(
    "/{todo_id}",
    response_model=TodoOut,
    status_code=HTTPStatus.OK,
    responses={
        404: {"model": ErrorSchema, "description": "Todo not found"},
        409: {"model": ErrorSchema, "description": "Todo title already exists"},
        422: {"model": ErrorSchema, "description": "Validation Error"},
    },
)
async def update_todo_put(
    todo_id: int,
    request: TodoCreate,
    db: Session = Depends(get_db),
) -> TodoOut:
    todo = TodoService(db).update_todo_put(todo_id, request)
    return todo


@todo_router.patch(
    "/{todo_id}",
    response_model=TodoOut,
    status_code=HTTPStatus.OK,
    responses={
        404: {"model": ErrorSchema, "description": "Todo not found"},
        409: {"model": ErrorSchema, "description": "Todo title already exists"},
        422: {"model": ErrorSchema, "description": "Validation Error"},
    },
)
async def update_todo_patch(
    todo_id: int,
    request: TodoUpdate,
    db: Session = Depends(get_db),
) -> TodoOut:
    todo = TodoService(db).update_todo_patch(todo_id, request)
    return todo


@todo_router.delete(
    "/{todo_id}",
    status_code=HTTPStatus.NO_CONTENT,
    responses={
        404: {"model": ErrorSchema, "description": "Todo not found"},
        422: {"model": ErrorSchema, "description": "Validation Error"},
    },
)
async def delete_todo(
    todo_id: int,
    db: Session = Depends(get_db),
) -> Response:
    TodoService(db).delete_todo(todo_id)
    return Response(status_code=HTTPStatus.NO_CONTENT)
