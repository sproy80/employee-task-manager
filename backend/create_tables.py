import asyncio
from app.database.base import Base
from app.database.session import engine

#Import models so SQLALchemy knows about them and can create the tables
from app.models.employee import Employee
from app.models.task import Task


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

if __name__ == "__main__":
    asyncio.run(create_tables())