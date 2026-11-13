from app.core.database.connection import Base
from sqlalchemy import Column,Integer,String,ForeignKey,Float,DateTime,func
from sqlalchemy.orm import relationship

class Order(Base):
    __tablename__ ="orders"
    id=Column(Integer,primary_key=True)
    customer_id=Column(Integer,ForeignKey("customers.id"), nullable=False)
    #user_id=Column(Integer,ForeignKey("users.id"),nullable=False)
    montant_total=Column(Float,nullable=False)
    oder_date=Column(DateTime(timezone=True),server_default=func.now(),nullable=False)
    status=Column(String,default="pending")

    #relationship
    order_item=relationship("OrderItem", back_populates="order")
    customer=relationship("Customer",back_populates="order")
    #user=relationship("User",back_populates="orders")


class OrderItem(Base):
    __tablename__ ="orders_items"
    id=Column(Integer,primary_key=True,nullable=False)
    order_id=Column(Integer,ForeignKey("orders.id"), nullable=False)
    product_id=Column(Integer,ForeignKey("products.id"),nullable=False)
    quantity=Column(Integer,nullable=False)
    unit_price=Column(Float,nullable=False)

    #relationship
    order=relationship("Order",back_populates="order_item")
    product=relationship("Product",back_populates="order_item")
