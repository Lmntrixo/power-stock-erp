from sqlalchemy.orm import Session
from app.purchase.models import Purchase,PurchaseItem
from app.purchase.schemas import PurchaseCreate,PurchaseResponse,PurchaseItemCreate,PurchaseItemResponse
from app.purchase.purchase_repository import PurchaseRepository
from app.purchase.purchase_service import PurchaseService
from app.core.database.dependancies import get_db
from fastapi import APIRouter, Depends,HTTPException,status

router = APIRouter(prefix="/purchase", tags=["purchase"])

@router.post("",response_model=PurchaseResponse,status_code=201)
def create_purchases(data:PurchaseCreate,db:Session=Depends(get_db)):
    try:
        purchase =PurchaseService(db).create_purchase(data,repository)
        return purchase
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=str(exc)) from exc