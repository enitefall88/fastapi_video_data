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