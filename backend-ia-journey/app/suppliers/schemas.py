from pydantic import BaseModel, Field, EmailStr
from datetime import datetime

class SupplierCreate(BaseModel):
    name: str
    email: EmailStr
    telephone: str
    adresse:str
    is_active: bool | None
    
class SupplierUpdate(SupplierCreate):
    name: str
    email: EmailStr
    telephone: str
    is_active:  bool
    
class SupplierResponse(SupplierCreate):
    id: int
    name:  str
    adresse: str
    created_at: datetime

