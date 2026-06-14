from datetime import date
from typing import Optional

from pydantic import BaseModel


class AssetCreate(BaseModel):
    asset_id: str
    hostname: Optional[str] = None
    serial_number: Optional[str] = None
    asset_type: Optional[str] = None
    vendor: Optional[str] = None
    model: Optional[str] = None
    os_name: Optional[str] = None
    os_version: Optional[str] = None
    purchase_date: Optional[date] = None
    invoice_number: Optional[str] = None
    description: Optional[str] = None


class AssetResponse(AssetCreate):
    id: str
    status: str

    class Config:
        from_attributes = True