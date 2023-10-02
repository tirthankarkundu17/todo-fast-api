import uuid
from typing import List

from app.model.todo import Todo

todos_db: List[Todo] = []


async def read_todos():
    return todos_db


async def create_todo(todo: Todo):
    todo.id = str(uuid.uuid4())
    todos_db.append(todo)
    return todo


async def read_todo(todo_id: str):
    for todo in todos_db:
        if todo.id == todo_id:
            return todo
    return None


async def delete_todo(todo_id: str):
    t = None
    for todo in todos_db:
        if todo.id == todo_id:
            t = todo
    if t is not None:
        todos_db.remove(t)
    else:
        return None
