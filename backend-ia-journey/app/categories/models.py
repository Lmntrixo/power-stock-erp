from sqlalchemy import Column,Integer,String, DateTime,func
from app.core.database.connection import Base
from sqlalchemy.orm import relationship

class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer,primary_key=True,autoincrement=True)
    name= Column(String,nullable=False,unique=True)
    description = Column(String(255),nullable=True)
    created_at = Column(DateTime(timezone=True),server_default=func.now(), nullable=False)

    products = relationship("Product", back_populates="category")