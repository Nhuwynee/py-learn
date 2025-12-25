from datetime import datetime
from pydantic import BaseModel, ConfigDict


class TodoOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    description: str | None
    priority: int
    done: bool
    created_at: datetime
    updated_at: datetime
