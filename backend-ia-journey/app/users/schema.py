from pydantic import BaseModel, Field, EmailStr

class RoleEnum(BaseModel):
    "admin",
    "manager",
    "employee"

class UserCreate(BaseModel):
    name: str=Field(...,min_length=2,max_length=150)
    email: EmailStr
    password_hash:str
    