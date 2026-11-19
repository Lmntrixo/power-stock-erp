from pydantic import BaseModel, Field,ConfigDict
from uuid import UUID as uuid
from typing import Optional

class ShopCreate(BaseModel):
    #entreprise_id: uuid
    name: str
    ville: str
    adresse: str
    phone_number: str
    is_active: bool

    model_config = ConfigDict(extra="forbid")

class ShopUpdate(BaseModel):
    name:Optional[str]=Field(None)
    ville:Optional[str]=Field(None)
    adresse:Optional[str]=Field(None)
    phone_number:Optional[str]=Field(None)
    is_active:bool=Field(default=True)

class ShopResponse(BaseModel):
    id:uuid
    entreprise_id: uuid
    name: str
    ville:str
    adresse: str
    phone_number: str
    is_active: bool

    class Config:
        from_attributes=True
