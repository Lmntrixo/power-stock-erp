from sqlalchemy import UUID, ForeignKey,Integer,Boolean,String,Enum,DATETIME,Column,func,DateTime
from app.core.database.connection import Base
from app.core.models import BaseModelMixin,TenantMixin
from sqlalchemy.orm import relationship
from app.users.schema import RoleEnum


class APPUser(BaseModelMixin,TenantMixin,Base):
    __tablename__ = "app_users"
    #id = Column(Integer,primary_key=True, autoincrement=True)
    name = Column(String(255),nullable=False)
    email = Column(String(255),nullable=True, unique=True)
    phone = Column(String(255),nullable=True)
    password_hash = Column(String(255),nullable=False)
    role = Column(Enum(RoleEnum),nullable=False)
    is_active = Column(Boolean,nullable=False, default=True)
    deleted_at=Column(DateTime(timezone=True),server_default=func.now(),nullable=True)
    created_at = Column(DateTime(timezone=True),server_default=func.now(), nullable=False)
    is_login_at = Column(DateTime(timezone=True),server_default=func.now(), nullable=False)
    #relationship
    #orders=relationship("Order", back_populates="user")
    #stockmovement=relationship("StockMovement",back_populates="user")

class UserShop(BaseModelMixin,TenantMixin,Base):
    __tablename__ = "user_shops"
    user_id = Column(UUID(as_uuid=True),ForeignKey("app_users.id", ondelete="CASCADE"),nullable=False)
    shop_id = Column(UUID(as_uuid=True),ForeignKey("shops.id",ondelete="CASCADE"),nullable=False)
