import uuid

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import String
from sqlalchemy.sql import func

from app.database.base import Base


class Employee(Base):
    __tablename__ = "employees"

    id = Column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )

    employee_id = Column(
        String(50),
        unique=True,
        nullable=False
    )

    employee_name = Column(
        String(255),
        nullable=False
    )

    email = Column(
        String(255),
        unique=True
    )

    department = Column(
        String(255)
    )

    location = Column(
        String(255)
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )