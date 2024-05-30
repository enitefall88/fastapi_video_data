from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class STaskAdd(BaseModel):
    name: str
    description: str | None

class STask(STaskAdd):
    id: int

@app.post("/tasks/")
async def add_task(
        task: STaskAdd,
):
    return {"ok": True}

# @app.get("/tasks")
# async def get_tasks():
#     task = STask(name="Record a new video", description="Task 1")
#     return {"data": task}


