#from pydantic import BaseModel, Field
from app.core.database.connection import Base
from sqlalchemy import Column, String, Integer, DateTime, func
from sqlalchemy.orm import relationship
#from datetime import datetime

class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer,primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String(255), nullable=False,unique=True,index=True)
    phone = Column(String,nullable=True)
    created_at = Column(DateTime(timezone=True),server_default=func.now(), nullable=False)

    #relationship
    #order=relationship("Order",back_populates="customer")