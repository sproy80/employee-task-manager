from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession 

from app.database.dependencies import get_db
from app.schemas.employee import EmployeeCreate, EmployeeResponse, EmployeeUpdate
from app.services.employee_service import EmployeeService

router = APIRouter(
    prefix="/employees",
    tags=["employees"]
)

employee_service = EmployeeService()

@router.post("/", response_model=EmployeeResponse)
async def create_employee(employee: EmployeeCreate, db: Annotated[AsyncSession, Depends(get_db)]):
    db_employee = await employee_service.create_employee(db, employee)
    return db_employee


@router.get("/{employee_id}", response_model=EmployeeResponse)
async def get_employee(employee_id: int, db: Annotated[AsyncSession, Depends(get_db)]):
    db_employee = await employee_service.get_employee_by_id(db, employee_id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee


@router.get("/", response_model=list[EmployeeResponse])
async def get_all_employees(db: Annotated[AsyncSession, Depends(get_db)]):
    employees = await employee_service.get_all_employee(db)
    return employees



@router.put("/{employee_id}",response_model=EmployeeResponse)
async def update_employee(
    employee_id:int,
    employee_update: EmployeeUpdate,
    db: AsyncSession = Depends(get_db)
):
    employee = await employee_service.update_employee(db, employee_id, employee_update)

    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    
    return employee
