from fastapi import FastAPI
from sqlalchemy import Boolean, Column, Integer,String, DateTime,ForeignKey,func
from sqlalchemy.orm import relationship
from app.core.database.connection import Base

class Supplier(Base):
    __tablename__ = "suppliers"
    id = Column(Integer, primary_key=True,nullable=False)
    name = Column(String,nullable=False,unique=True)
    #Achat_id = Column(Integer,ForeignKey("achats.id"), nullable=False)
    email = Column(String(150), nullable=False, unique=True)
    telephone = Column(String,nullable=False, unique=True)
    adresse = Column(String,nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True),server_default=func.now(),nullable=False)
    update_at = Column(DateTime(timezone=True),server_default=func.now(), nullable=False)
    #achat = relationship(Achats, back_populates="supplier")
    