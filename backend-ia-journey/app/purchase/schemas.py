from pydantic import BaseModel,Field


class PurchaseCreate(BaseModel):
    supplier_id: int
    status: str = Field(..., description="Status of the purchase")
    purchase_date: str = Field(..., description="Date of the purchase in YYYY-MM-DD format")
    items: list[PurchaseItemCreate] = Field(...,description="list of purchase items associated with the purchase")

class PurchaseItemCreate(BaseModel):
    purchase_id: int
    product_id: int
    quantity: int = Field(..., description="Quantity of the product in the purchase item")
    unit_cost: float = Field(..., description="price for unit product in the purchase item")

class PurchaseResponse(BaseModel):
    id:int
    supplier_id:int
    status:str

class PurchaseItemResponse(BaseModel):
    purchase_id:int
    product_id:int
    quantity:int
    unit_cost:float


