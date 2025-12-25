from typing import TypeVar, Generic, Type, Optional, List
from sqlalchemy.orm import Session

ModelType = TypeVar("ModelType")


class BaseRepository(Generic[ModelType]):

    def __init__(self, model: Type[ModelType]):
        self.model = model

    def get_by_id(self, db: Session, id: int) -> Optional[ModelType]:
        return db.query(self.model).filter(self.model.id == id).first()

    def get_all(self, db: Session, skip: int = 0, limit: int = 100) -> List[ModelType]:
        return db.query(self.model).offset(skip).limit(limit).all()

    def create(self, db: Session, obj_in: dict) -> ModelType:
        db_obj = self.model(**obj_in)
        db.add(db_obj)
        db.flush()
        db.refresh(db_obj)
        return db_obj

    def update(self, db: Session, obj: ModelType, obj_in: dict) -> ModelType:
        for key, value in obj_in.items():
            setattr(obj, key, value)
        db.add(obj)
        db.flush()
        db.refresh(obj)
        return obj

    def delete(self, db: Session, id: int) -> bool:
        obj = self.get_by_id(db, id)
        if obj:
            db.delete(obj)
            db.flush()
            return True
        return False
