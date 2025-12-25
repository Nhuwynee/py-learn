from pydantic import BaseModel, Field
from typing import Optional


class TodoCreate(BaseModel):
    title: str = Field(..., min_length=3)
    description: str | None = None
    priority: int = Field(..., ge=1, le=5)
    done: bool = False

    model_config = {
        "str_strip_whitespace": True
    }


class TodoUpdate(BaseModel):
    title: str | None = Field(None, min_length=3)
    description: str | None = None
    priority: int | None = Field(None, ge=1, le=5)
    done: bool | None = None

    model_config = {
        "str_strip_whitespace": True
    }


class TodoFilter(BaseModel):
    done: Optional[bool] = None
    keyword: Optional[str] = None
    offset: int = Field(0, ge=0)
    limit: int = Field(10, ge=1, le=100)

    model_config = {
        "str_strip_whitespace": True
    }
