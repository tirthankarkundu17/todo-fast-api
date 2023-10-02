from fastapi import FastAPI

from .router import todo

app = FastAPI(
    title="Todos API",
    description="Todos API with in memory Database",
)

app.include_router(todo.router)


@app.get("/", tags=["health"])
async def root():
    return {"status": "Success", "message": "App is running!"}
