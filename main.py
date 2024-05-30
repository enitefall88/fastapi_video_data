from fastapi import FastAPI
from pydantic import BaseModel
from typing import Annotated
from fastapi import Depends

app = FastAPI()


class STaskAdd(BaseModel):
    name: str
    description: str | None

class STask(STaskAdd):
    id: int

tasks = []

@app.post("/tasks/")
async def add_task(
        task: Annotated[STaskAdd, Depends()],
):
    tasks.append(task)
    return {"ok": True}

# @app.get("/tasks")
# async def get_tasks():
#     task = STask(name="Record a new video", description="Task 1")
#     return {"data": task}


