from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_tables, drop_tables
from  router import router as tasks_router
@asynccontextmanager
async def lifespan(app: FastAPI):
    await drop_tables()
    print("Dropping tables")
    await create_tables()
    print("Database tables have been created")
    yield
    print("Shutting down lifespan...")


app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)









