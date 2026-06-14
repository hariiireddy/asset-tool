from pydantic import BaseModel
from typing import Optional


class EmployeeCreate(BaseModel):
    employee_id: str
    employee_name: str
    email: Optional[str] = None
    department: Optional[str] = None
    location: Optional[str] = None


class EmployeeResponse(EmployeeCreate):
    id: str

    class Config:
        from_attributes = True