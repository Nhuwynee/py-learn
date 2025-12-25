from pydantic import BaseModel


class ErrorSchema(BaseModel):
    success: bool = False
    error: dict

