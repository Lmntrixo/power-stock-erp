from sqlalchemy import Integer, Column,Boolean,String,Numeric, ForeignKey,DateTime,func
from sqlalchemy.orm import relationship
from app.core.database.connection import Base

class Product(Base):
    __tablename__ = "products"
    id= Column(Integer,primary_key=True,autoincrement=True,index=True)
    categorie_id =Column(Integer,ForeignKey("categories.id"),nullable=False)
#purchase_item_id = Column(Integer,ForeignKey("purchase_items.id"))
    name = Column(String(150),nullable=False,index=True)
    description = Column(String,nullable=True)
    sku= Column(String(50),nullable=False,unique=True)
    unit_price = Column(Numeric, nullable=False, default=0)
    stock_quantity = Column(Integer,nullable=False,default=0)
    is_active = Column(Boolean, nullable=False, default=True)
    created_at = Column(DateTime(timezone=True),server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True),server_default=func.now(), nullable=False)
    #relationship
    category =relationship("Category",back_populates="products")
    purchase_item = relationship("PurchaseItem",back_populates="product")
    order_item=relationship("OrderItem",back_populates="product")
    stockmovement=relationship("StockMovement",back_populates="product")