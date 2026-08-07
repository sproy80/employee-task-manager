from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.employee import Employee
from app.schemas.employee import EmployeeCreate, EmployeeUpdate


class EmployeeRepository:

    async def create(self, db: AsyncSession, employee: EmployeeCreate):
        db_employee = Employee(**employee.model_dump())
        db.add(db_employee)
        await db.commit()
        await db.refresh(db_employee)
        return db_employee

    async def get_all(self, db: AsyncSession):
        result = await db.execute(select(Employee))
        return result.scalars().all()

    async def get_by_id(self, db: AsyncSession, employee_id: int):
        result = await db.execute(
            select(Employee).where(Employee.id == employee_id)
        )
        return result.scalar_one_or_none()

    # -----------------------------
    # NEW METHOD
    # -----------------------------
    async def update(
        self,
        db: AsyncSession,
        employee: Employee,
        employee_update: EmployeeUpdate,
    ):
        update_data = employee_update.model_dump(exclude_unset=True)

        for field, value in update_data.items():
            setattr(employee, field, value)

        await db.commit()
        await db.refresh(employee)

        return employee


    async def delete(
        self,
        db: AsyncSession,
        employee: Employee,
    ) -> None:

        await db.delete(employee)
        await db.commit()