from fastapi import FastAPI
from pydantic import BaseModel
from typing import Annotated
from fastapi import Depends
from contextlib import asynccontextmanager
from database import create_tables, drop_tables
@asynccontextmanager
async def lifespan(app: FastAPI):
    await drop_tables()
    print("Dropping tables")
    await create_tables()
    print("Database tables have been created")
    yield
    print("Shutting down lifespan...")


app = FastAPI(lifespan=lifespan)




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


