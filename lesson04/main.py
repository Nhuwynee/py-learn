from fastapi import FastAPI
from lesson04.controllers.todo_controller import todo_router

app = FastAPI()

app.include_router(todo_router)
