from pydantic import BaseModel
from typing import Union


class Todo(BaseModel):
    id: Union[str, None] = None
    todo: str
