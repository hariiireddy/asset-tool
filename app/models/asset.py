import uuid

from sqlalchemy import Column
from sqlalchemy import Date
from sqlalchemy import DateTime
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy.sql import func

from app.database.base import Base


class Asset(Base):
    __tablename__ = "assets"

    id = Column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )

    asset_id = Column(
        String(50),
        unique=True,
        nullable=False
    )

    hostname = Column(
        String(255)
    )

    serial_number = Column(
        String(255)
    )

    asset_type = Column(
        String(100)
    )

    vendor = Column(
        String(100)
    )

    model = Column(
        String(255)
    )

    os_name = Column(
        String(100)
    )

    os_version = Column(
        String(100)
    )

    purchase_date = Column(
        Date
    )

    invoice_number = Column(
        String(100)
    )

    description = Column(
        Text
    )

    status = Column(
        String(50),
        default="Offline"
    )

    last_seen = Column(
        DateTime(timezone=True)
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