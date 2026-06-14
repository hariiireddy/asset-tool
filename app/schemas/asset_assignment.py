from datetime import date

from pydantic import BaseModel


class AssetAssignmentCreate(BaseModel):
    asset_id: str
    employee_id: str
    assigned_date: date


class AssetAssignmentResponse(AssetAssignmentCreate):
    id: str
    status: str

    class Config:
        from_attributes = True