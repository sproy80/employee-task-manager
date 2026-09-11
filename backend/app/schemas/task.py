from datetime import datetime
from pydantic import BaseModel, ConfigDict

class TaskBase(BaseModel):
    title: str
    description: str | None= None
    status: str = "Pending"
    employee_id: int

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    title: str | None = None
    description: str | None = None
    status: str | None = None
    employee_id: int | None = None

class TaskResponse(TaskBase):
    id: int
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)

    