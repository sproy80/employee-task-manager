from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr

#Common fields shared by multiple schemas.
class EmployeeBase(BaseModel):
    name: str
    department: str
    email: EmailStr

#Used when creating an employee.
class EmployeeCreate(EmployeeBase):
    pass

#Used when updating an employee.
class EmployeeUpdate(EmployeeBase):
    pass

# Used when returning data from the API.
class EmployeeResponse(EmployeeBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)