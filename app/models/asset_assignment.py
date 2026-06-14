import uuid

from sqlalchemy import Column
from sqlalchemy import Date
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import relationship

from app.database.base import Base


class AssetAssignment(Base):
    __tablename__ = "asset_assignments"

    id = Column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )

    asset_id = Column(
        String(36),
        ForeignKey("assets.id"),
        nullable=False
    )

    employee_id = Column(
        String(36),
        ForeignKey("employees.id"),
        nullable=False
    )

    assigned_date = Column(
        Date,
        nullable=False
    )

    returned_date = Column(
        Date
    )

    status = Column(
        String(50),
        default="Assigned"
    )

    asset = relationship("Asset")

    employee = relationship("Employee")