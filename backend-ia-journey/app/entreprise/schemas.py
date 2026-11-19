from pydantic import BaseModel, Field,ConfigDict
from typing import Optional
from uuid import UUID as uuid

class EntrepriseCreate(BaseModel):
    #id: Optional[uuid] = None
    name: str = Field(..., max_length=100)
    address: str = Field(..., max_length=200)
    email: str = Field(..., max_length=100)
    phone_number: str = Field(..., max_length=20)
    business_type: str = Field(..., max_length=100)
    currency: str = Field(..., max_length=10)
    is_active: bool = Field(default=True)

    model_config = ConfigDict(from_attributes=True)

class EntrepriseUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=100)
    address:Optional[str] = Field(None, max_length=200)
    email: Optional[str] = Field(None, max_length=100)
    phone_number: Optional[str] = Field(None, max_length=20)
    business_type: Optional[str] = Field(None, max_length=100)
    currency: Optional[str] = Field(None, max_length=10)
    is_active: bool = Field(default=True)

class EntrepriseResponse(BaseModel):
    id: uuid
    name: str
    address: str
    email: str
    phone_number: str
    business_type: str
    currency: str
    is_active: bool

    class Config:
        from_attributes = True