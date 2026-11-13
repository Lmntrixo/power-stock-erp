from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime

class CategoryCreate(BaseModel):
    name: str= Field(...,min_length=2,max_length=50)
    description: str

    model_config =  ConfigDict(extra="forbid")

class CategoryResponse(CategoryCreate):
    id:  int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

