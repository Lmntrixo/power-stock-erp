from sqlalchemy import Integer,String,DATETIME,Column,func,DateTime
from app.core.database.connection import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True, autoincrement=True)
    name = Column(String(255),nullable=False)
    email = Column(String(255),nullable=False, unique=True)
    password_hash = Column(String(255),nullable=False)
    role = Column(String(30),nullable=False)
    is_active = Column(bool,nullable=False, default=True)
    created_at = Column(DateTime(timezone=True),server_default=func.now(), nullable=False)

    #relationship
    orders=relationship("Order", back_populates="user")
    stockmovement=relationship("StockMovement",back_populates="user")