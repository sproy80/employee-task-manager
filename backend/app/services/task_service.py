#task_service.py
from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.task_repository import TaskRepository
from app.schemas.task import TaskCreate, TaskUpdate
from app.models.task import Task
from app.core.exceptions.exceptions import TaskNotFoundException, EmployeeNotFoundException
from app.repositories.employee_repository import EmployeeRepository
import logging

logger = logging.getLogger(__name__)


class TaskService:

    def __init__(self):
         self.repository = TaskRepository()
         self.employee_repository = EmployeeRepository()


    
    async def create_task(self, db: AsyncSession,
                              task: TaskCreate,) -> Task:

            employee = await self.employee_repository.get_by_id(db,task.employee_id)
            if employee is None:
                logger.warning(
                    "Task creation failed | employee_id=%s not found",
                    task.employee_id,
                )
                raise EmployeeNotFoundException(task.employee_id)

            # return await self.repository.create(db, task)
            created_task = await self.repository.create(db, task)
            logger.info(
                "Task created successfully | task_id=%s | employee_id=%s",
                created_task.id,
                created_task.employee_id,
            )

            return created_task

    

    
    async def get_all_tasks(self, db: AsyncSession) -> list[Task]:
        return await self.repository.get_all(db)
    
    
    async def get_task_by_id(self, db: AsyncSession, task_id: int):
        task = await self.repository.get_by_id(db, task_id)
        if task is None:
            raise TaskNotFoundException(task_id)

        return task
        
    
    async def update_task(
              self,
              db: AsyncSession,
              task_id: int,
              task_update: TaskUpdate
              
        )->Task | None:
        task = await self.repository.get_by_id(db, task_id)
        if task is None:
            raise TaskNotFoundException(task_id)

        return await self.repository.update(db, task, task_update)

    async def delete_task(
        self,
        db: AsyncSession,
        task_id: int,
    ) -> bool:

        task = await self.repository.get_by_id(
            db,
            task_id,
        )

        if task is None:
            raise TaskNotFoundException(task_id)

        await self.repository.delete(
            db,
            task,
        )

        return True