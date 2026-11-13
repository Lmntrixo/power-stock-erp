from pydantic import BaseModel, Field, ConfigDict
from app.core.database.connection import Base
from datetime import datetime

class ProductCreate(BaseModel):
    name: str
    description: str
    sku: str
    unit_price: float
    stock_quantity: int
    categorie_id: int

    model_config =ConfigDict(extra="forbid")

class ProductResponse(ProductCreate):
    id: int
    created_at: datetime
    updated_at: datetime
    is_active: bool
    stock_quantity: int
    categorie_id: int


    model_config = ConfigDict(from_attributes=True)
