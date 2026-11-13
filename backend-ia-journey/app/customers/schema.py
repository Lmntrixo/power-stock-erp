from pydantic import BaseModel,Field, EmailStr, ConfigDict
from datetime import datetime


class CustomerCreate(BaseModel):
    name: str=Field(...,min_length=2,max_length=150)
    email: EmailStr
    phone: str | None = None

    model_config =ConfigDict(extra="forbid")

class CustomerResponse(CustomerCreate):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)