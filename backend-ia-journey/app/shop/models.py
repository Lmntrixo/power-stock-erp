from sqlalchemy.orm import relationship
from sqlalchemy import Integer,Boolean,String,ForeignKey,func,Column,Float,DateTime
from app.core.database.connection import Base
from app.core.models import BaseModelMixin,TenantMixin

class Shop(BaseModelMixin,TenantMixin,Base):
    __tablename__ = "shops"
    #id = Column(Integer,primary_key=True)
    #entreprise_id = Column(Integer,ForeignKey("entreprises.id"),nullable=False,index=True)
    name = Column(String(150),nullable=False)
    ville = Column(String(150),nullable=False)
    adresse = Column(String(255),nullable=True)
    phone_number = Column(String(20),nullable=True)
    is_active = Column(Boolean,default=True,nullable=False)

