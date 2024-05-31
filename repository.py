from database import new_session, TaskOrm
from main import STaskAdd

class TaskRepository:
    @classmethod
    async def add_one(cls, data: STaskAdd) -> int:
        async with new_session() as session:
            task_dict = data.model_dump()

            task = TaskOrm(**task_dict)
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id

    @classmethod
    async def find_all_tasks(cls):
        async with new_session() as session:
            query = session.query(TaskOrm)
            result = await session.execute(query)
            task_models = result.scalars().all()
            return task_models