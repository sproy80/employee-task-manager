from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate


class TaskRepository:
    async def create(
            self,
            db: AsyncSession,
            task: TaskCreate,

    ) -> Task:

        db_task = Task(
            title = task.title,
            description = task.description,
            status = task.status,
            employee_id = task.employee_id,

        )

        db.add(db_task)
        await db.commit()
        await db.refresh(db_task)

        return db_task

    async def get_all(self, db: AsyncSession) -> list[Task]:
        result = await db.execute(select(Task))
        return result.scalars().all()

    async def get_by_id(
        self,
        db: AsyncSession,
        task_id: int,
    ) -> Task | None:
        result = await db.execute(
            select(Task).where(Task.id == task_id)
        )
        return result.scalar_one_or_none()

    async def update(
            self,
            db: AsyncSession,
            task: Task,
            task_update: TaskUpdate,
    ) -> Task:

        update_data = task_update.model_dump(exclude_unset=True)

        for field, value in update_data.items():
            setattr(task, field, value)

        await db.commit()
        await db.refresh(task)

        return task


    async def delete(
            self,
            db: AsyncSession,
            task: Task,
    ) -> None:
        await db.delete(task)
        await db.commit()