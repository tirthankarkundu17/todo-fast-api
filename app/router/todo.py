from fastapi import APIRouter, HTTPException

import app.service.todo as todo_service
from app.model.todo import Todo

router = APIRouter(
    prefix="/todos",
    tags=["todos"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def read_todos():
    return await todo_service.read_todos()


@router.post("/")
async def create_todo(todo: Todo):
    return await todo_service.create_todo(todo)


@router.get("/{todo_id}")
async def read_todo(todo_id: str):
    todo = await todo_service.read_todo(todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


@router.delete("/{todo_id}", status_code=204)
async def delete_todo(todo_id: str):
    todo = await todo_service.read_todo(todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    await todo_service.delete_todo(todo_id)
