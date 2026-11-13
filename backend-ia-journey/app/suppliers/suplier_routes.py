from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from app.suppliers.schemas import SupplierCreate,SupplierResponse,SupplierUpdate
from app.suppliers.models import Supplier
from app.suppliers.supplier_repository import SupplierRepository
from app.suppliers.suplier_service import Create_suppier,list_allSuppliers,get_one_supplier_by_id
from  app.core.database.dependancies import get_db

router = APIRouter(prefix="/suppliers",tags=["suppliers"])

@router.post("",response_model=SupplierResponse,status_code=201)
def Create_suppliers(data:SupplierCreate, db:Session=Depends(get_db)):
    repository = SupplierRepository(db)
    try:
        supplier = Create_suppier(data,repository)
        return supplier
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=str(exc)) from exc

@router.get("",response_model=list[SupplierResponse],status_code=200)
def list_all_suppliers(db:Session=Depends(get_db)):
    repository = SupplierRepository(db)
    try:
        all_supliers = list_allSuppliers(repository)
        return all_supliers
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=str(exc)) from exc
@router.get("/{suplier_id}",response_model=SupplierResponse,status_code=200)
def suplier_by_id(supplier_id:int,db:Session=Depends(get_db)):
    repository = SupplierRepository(db)
    try:
        suplier = get_one_supplier_by_id(supplier_id,repository)
        return suplier
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=str(exc)) from exc


