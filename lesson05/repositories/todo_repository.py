from typing import Optional, List
from sqlalchemy.orm import Session
from sqlalchemy import func

from models.todo import Todo
from repositories.base_repository import BaseRepository


class TodoRepository(BaseRepository[Todo]):

    def __init__(self):
        super().__init__(Todo)

    def get_by_title(self, db: Session, title: str) -> Optional[Todo]:
        return db.query(self.model).filter(
            func.lower(self.model.title) == title.lower()
        ).first()

    def search(
        self,
        db: Session,
        *,
        done: Optional[bool] = None,
        keyword: Optional[str] = None,
        offset: int = 0,
        limit: int = 100
    ) -> List[Todo]:
        query = db.query(self.model)

        if done is not None:
            query = query.filter(self.model.done == done)

        if keyword:
            query = query.filter(
                self.model.title.ilike(f"%{keyword}%")
            )

        return query.offset(offset).limit(limit).all()
