from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from app.customers.schema import CustomerCreate,  CustomerResponse
from app.customers.customer_repository import CustomerRepository
from app.customers import models
from app.customers.customer_service import create_customer, list_customers, get_customer_by_id
from app.core.database.dependancies import get_db

router = APIRouter(prefix="/customers", tags=["Customers"])

@router.post("", response_model=CustomerResponse,status_code=201)
def create_customer_route(data:CustomerCreate, db:Session=Depends(get_db)):
    repository = CustomerRepository(db)
    try:
        customer = create_customer(data,repository)
        return customer
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=str(exc)) from exc

@router.get("",response_model=list[CustomerResponse],status_code=200)
def get_all_customers(db:Session=Depends(get_db)):
    repository = CustomerRepository(db)
    try:
        return list_customers(repository)
        
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No customesr founds")
@router.get("/{customer_id}",response_model=CustomerResponse, status_code=200)
def get_customer_byid(customer_id:int, db:Session=Depends(get_db)):
    repository = CustomerRepository(db)
    try:
        customer=get_customer_by_id(customer_id, repository)
        return customer
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=str(exc)) from exc
