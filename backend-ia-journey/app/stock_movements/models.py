from app.core.database.connection import Base
from sqlalchemy import Integer,String,ForeignKey,func,DateTime,Column
from sqlalchemy.orm import relationship

class StockMovement(Base):
    __tablename__ ="stock_movements"
    id=Column(Integer,primary_key=True)
    product_id=Column(Integer,ForeignKey("products.id"),nullable=False)
    #user_id=Column(Integer,ForeignKey("users.id"),nullable=False)
    movement_type=Column(String,default="OUT",nullable=False)
    quantity=Column(Integer,nullable=False)
    reason=Column(String)
    created_at=Column(DateTime(timezone=True),server_default=func.now(),nullable=False)

    #relationship
   # user=relationship("User",back_populates="stockmovement")
    product=relationship("Product",back_populates="stockmovement")