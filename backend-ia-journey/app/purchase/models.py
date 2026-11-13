from app.core.database.connection import Base
from sqlalchemy import Column,Integer,String,ForeignKey,func,DateTime,Float
from sqlalchemy.orm import relationship

class Purchase(Base):
    __tablename__ = "purchases"
    id = Column(Integer,primary_key=True)
    supplier_id = Column(Integer,ForeignKey("suppliers.id"))
    #user_id = Column(Integer,ForeignKey("users.id"))
    status = Column(String, default="pending")
    purchase_date = Column(DateTime(timezone=True),server_default=func.now(), nullable=False)

    #relationship
    purchase_item =relationship("PurchaseItem",back_populates="purchase")

class PurchaseItem(Base):
    __tablename__ = "purchase_items"
    id = Column(Integer,primary_key=True)
    purchase_id = Column(Integer,ForeignKey("purchases.id"))
    product_id = Column(Integer,ForeignKey("products.id"))
    quantity = Column(Integer)
    unit_cost = Column(Float)

    #relationship
    purchase = relationship("Purchase",back_populates="purchase_item")
    product = relationship("Product", back_populates="purchase_item")