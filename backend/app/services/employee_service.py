#employee_service.py
from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.employee_repository import EmployeeRepository
from app.schemas.employee import EmployeeCreate, EmployeeUpdate
from app.models.employee import Employee


class EmployeeService:

    def __init__(self):
         self.repository = EmployeeRepository()


    
    async def create_employee(self, db: AsyncSession,
                              employee: EmployeeCreate,):
            
            return await self.repository.create(db, employee)

    

    
    async def get_all_employee(self, db: AsyncSession):
        return await self.repository.get_all(db)
    
    
    async def get_employee_by_id(self, db: AsyncSession, employee_id: int):
        return await self.repository.get_by_id(db, employee_id)
    
    async def update_employee(
              self,
              db: AsyncSession,
              employee_id: int,
              employee_update: EmployeeUpdate
              
        )->Employee | None:
        employee = await self.repository.get_by_id(db, employee_id)
        if employee is None:
            return None
        
        return await self.repository.update(db, employee, employee_update)