from fastapi import FastAPI

from configs.database import engine, Base
from controllers.todo_controller import todo_router
from middlewares.db_middleware import DBMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Todo API",
    description="FastAPI with PostgreSQL Database",
    version="1.0.0"
)

app.add_middleware(DBMiddleware)

app.include_router(todo_router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
