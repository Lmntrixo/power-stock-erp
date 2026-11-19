from enum import Enum
from uuid import UUID as uuid
from pydantic import BaseModel, Field, EmailStr, ConfigDict
from datetime import datetime
from typing import Optional

class RoleEnum(str, Enum):
    admin= "admin"
    manager="manager"
    cashier ="cashier"

class UserCreate(BaseModel):
    name: str=Field(...,min_length=2,max_length=150)
    email: Optional[EmailStr]=None
    password:str
    phone: Optional[str]=None
    role: RoleEnum
    is_active:bool=Field(default=True)
    #is_login_at: datetime

    model_config = ConfigDict(from_attributes=True)

class UserUpdate(BaseModel):
    name: Optional[str]=Field(None,min_length=2,max_length=150)
    email: Optional[EmailStr]=None
    #password:Optional[str]=Field(None)
    phone: Optional[str]=Field(None)
    role: Optional[RoleEnum]=None
    is_active:bool=None

class UserResponse(BaseModel):
    id:uuid
    name: str
    entreprise_id:uuid
    phone: Optional[str]=None
    role:RoleEnum
    is_active:bool
    is_login_at:Optional[datetime]=None
    deleted_at:Optional[datetime]

    model_config = ConfigDict(from_attributes=True)


    