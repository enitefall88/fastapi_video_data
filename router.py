from fastapi import APIRouter, Depends
from typing import Annotated
from schemas import STask, STaskAdd
from repository import  TaskRepository

router = APIRouter(
    prefix="/tasks",
)

@router.post("")
async def add_task(
        task: Annotated[STaskAdd, Depends()],
):
    task_id = await TaskRepository.add_one(task)
    return {"ok": True, "task_id": task_id}

@router.get("")
async def get_tasks():
    task = STask(name="Record a new video", description="Task 1")
    return {"data": task}