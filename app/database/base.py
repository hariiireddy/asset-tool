from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


# Import models so SQLAlchemy discovers them
from app.models.user import User
from app.models.employee import Employee
from app.models.asset import Asset
from app.models.asset_assignment import AssetAssignment