from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from sqlalchemy.orm import Session

from configs.database import SessionLocal


class DBMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        db: Session = SessionLocal()
        request.state.db = db

        try:
            response = await call_next(request)
            db.commit()
            return response
        except Exception as e:
            db.rollback()
            raise e
        finally:
            db.close()

db_middleware = DBMiddleware

