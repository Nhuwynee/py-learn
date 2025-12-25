from typing import List
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from repositories.todo_repository import TodoRepository
from schemas.request.todo_schema import TodoCreate, TodoUpdate, TodoFilter
from schemas.response.todo_out_schema import TodoOut


class TodoService:
    def __init__(self, db: Session):
        self.db = db
        self.repo = TodoRepository()

    def create_todo(self, data: TodoCreate) -> TodoOut:
        existing = self.repo.get_by_title(self.db, data.title)
        if existing:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"Todo with title '{data.title}' already exists"
            )

        todo_dict = data.model_dump()
        todo = self.repo.create(self.db, todo_dict)
        return TodoOut.model_validate(todo)

    def get_todo(self, todo_id: int) -> TodoOut:
        todo = self.repo.get_by_id(self.db, todo_id)
        if not todo:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Todo with id {todo_id} not found"
            )
        return TodoOut.model_validate(todo)

    def list_todos(self, filters: TodoFilter) -> List[TodoOut]:
        todos = self.repo.search(
            self.db,
            done=filters.done,
            keyword=filters.keyword,
            offset=filters.offset,
            limit=filters.limit
        )
        return [TodoOut.model_validate(todo) for todo in todos]

    def update_todo_put(self, todo_id: int, data: TodoCreate) -> TodoOut:
        todo = self.repo.get_by_id(self.db, todo_id)
        if not todo:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Todo with id {todo_id} not found"
            )

        if data.title.lower() != todo.title.lower():
            existing = self.repo.get_by_title(self.db, data.title)
            if existing:
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail=f"Todo with title '{data.title}' already exists"
                )

        todo_dict = data.model_dump()
        updated_todo = self.repo.update(self.db, todo, todo_dict)
        return TodoOut.model_validate(updated_todo)

    def update_todo_patch(self, todo_id: int, data: TodoUpdate) -> TodoOut:
        todo = self.repo.get_by_id(self.db, todo_id)
        if not todo:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Todo with id {todo_id} not found"
            )

        if data.title and data.title.lower() != todo.title.lower():
            existing = self.repo.get_by_title(self.db, data.title)
            if existing:
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail=f"Todo with title '{data.title}' already exists"
                )

        update_dict = data.model_dump(exclude_unset=True)
        updated_todo = self.repo.update(self.db, todo, update_dict)
        return TodoOut.model_validate(updated_todo)

    def delete_todo(self, todo_id: int) -> None:
        todo = self.repo.get_by_id(self.db, todo_id)
        if not todo:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Todo with id {todo_id} not found"
            )
        self.repo.delete(self.db, todo_id)
