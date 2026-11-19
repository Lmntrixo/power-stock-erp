from fastapi import APIRouter,HTTPException,status,Depends
from sqlalchemy.orm import Session
from app.products.models import Product
from app.products.product_repository import ProductRepsitory
from app.products.schema import ProductCreate,ProductResponse
from app.products.product_service import ProductService
from app.core.database.dependancies import get_db

router = APIRouter(prefix="/products", tags=["Products"])

@router.post("",response_model=ProductResponse,status_code=201)
def create_product_route(data:ProductCreate, db:Session=Depends(get_db)):
    
    try:
        product = ProductService(db).create_Product(data,repository)
        return product
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=str(exc)) from exc

@router.get("",response_model=list[ProductResponse], status_code=200)
def get_products_list(db:Session=Depends(get_db)):
  
    try:
        products_list =ProductService(db).get_all_products(repository)
        return products_list
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=str(exc)) from exc