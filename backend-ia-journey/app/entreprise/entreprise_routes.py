from app.entreprise.models import Entreprise
from app.entreprise.schemas import EntrepriseCreate,EntrepriseUpdate,EntrepriseResponse
from app.entreprise.entreprise_repository import EntrepriseRepository
from sqlalchemy.orm import Session
from app.entreprise.entreprise_service import EntrepriseService
from fastapi import HTTPException,status    
from fastapi import APIRouter,Depends
from app.core.database.dependancies import get_db,get_current_entreprise
from uuid import UUID as uuid

router = APIRouter(prefix="/entreprises",tags=["entreprises"])

@router.post("",response_model=EntrepriseResponse,status_code=201)
def entreprise_create(data:EntrepriseCreate,db:Session=Depends(get_db)):
    
    try:
        entreprise = EntrepriseService(db).create_entreprise(data)
        return entreprise
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=str(exc)) from exc

@router.get("",response_model=list[EntrepriseResponse],status_code=200)
def list_of_entreprise(db:Session=Depends(get_db)):
    
    try:
        liste = EntrepriseService(db).list_all_entreprise()
        return liste
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=str(exc)) from exc

@router.patch("/me",response_model=EntrepriseUpdate,status_code=201)
def update_entreprise_route(data:EntrepriseUpdate,db:Session=Depends(get_db),entreprise_id:uuid=Depends(get_current_entreprise)):
    try:
        return EntrepriseService(db).updating_entreprise(data,entreprise_id)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=str(exc)) from exc

@router.delete("",response_model=EntrepriseResponse,status_code=200)
def deleting_entreprise(db:Session=Depends(get_db),entreprise_id:uuid=Depends(get_current_entreprise)):
    try:
        return EntrepriseService(db).delete_an_enreprise(entreprise_id)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=str(exc)) from exc
