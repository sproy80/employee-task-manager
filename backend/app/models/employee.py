from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.base import Base  
from datetime import datetime, timezone  
from pydantic import BaseModel, EmailStr



class Employee(Base):
    __tablename__ = "employees"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    department: Mapped[str] = mapped_column(String(150), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
    tasks = relationship("Task", back_populates="employee")


class EmployeeCreate(BaseModel):
    name: str
    email: EmailStr
    department: str

class EmployeeResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    department: str
    created_at: datetime

    model_config = {
        "from_attributes": True
    }