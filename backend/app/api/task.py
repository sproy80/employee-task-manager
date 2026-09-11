#api/task.py

from fastapi import APIRouter, Depends, status
from fastapi.responses import Response
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated

from app.database.dependencies import get_db
from app.schemas.task import TaskCreate, TaskResponse, TaskUpdate
from app.services.task_service import TaskService


router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"],
)

task_service = TaskService()


@router.post(
    "/",
    response_model=TaskResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_task(
    task: TaskCreate,
    db: Annotated[AsyncSession, Depends(get_db)],
):
    return await task_service.create_task(db, task)


@router.get(
    "/",
    response_model=list[TaskResponse],
)
async def get_all_tasks(
    db: Annotated[AsyncSession, Depends(get_db)],
):
    return await task_service.get_all_tasks(db)


@router.get(
    "/{task_id}",
    response_model=TaskResponse,
)
async def get_task(
    task_id: int,
    db: Annotated[AsyncSession, Depends(get_db)],
):
    return await task_service.get_task_by_id(db, task_id)


@router.put(
    "/{task_id}",
    response_model=TaskResponse,
)
async def update_task(
    task_id: int,
    task_update: TaskUpdate,
    db: Annotated[AsyncSession, Depends(get_db)],
):
    return await task_service.update_task(
        db,
        task_id,
        task_update,
    )


@router.delete(
    "/{task_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_task(
    task_id: int,
    db: Annotated[AsyncSession, Depends(get_db)],
):
    await task_service.delete_task(
        db,
        task_id,
    )

    return Response(
        status_code=status.HTTP_204_NO_CONTENT
    )