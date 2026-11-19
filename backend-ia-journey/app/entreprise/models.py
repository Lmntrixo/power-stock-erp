from sqlalchemy import Column,Boolean, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from app.core.database.connection import Base
from app.core.models import BaseModelMixin,TenantMixin

class Entreprise(Base, BaseModelMixin):
    __tablename__ = "entreprises"
    #id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, unique=True)
    business_type = Column(String(255), nullable=False)
    address = Column(String(255), nullable=True)
    phone_number = Column(String(20), nullable=True)
    email = Column(String(255), nullable=True, unique=True)
    currency = Column(String(10),default="XAF", nullable=True)
    is_active = Column(Boolean, default=True, nullable=False)


    # Relationships
    # Add any relationships if needed in the future