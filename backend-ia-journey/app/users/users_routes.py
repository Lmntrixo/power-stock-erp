from fastapi import APIRouter,Depends,HTTPException,status
from app.users.users_service import APPUserService
from app.users.schema import UserCreate,UserResponse,UserUpdate
from uuid import UUID as uuid
from sqlalchemy.orm import Session
from app.core.database.dependancies import get_current_entreprise,get_db,get_current_user
from app.core.security import hash_password
from app.users.model import APPUser

router=APIRouter(prefix="/users",tags=["users"])

@router.post("",response_model=UserResponse,status_code=201)
def creating_user(data:UserCreate, entreprise_id:uuid=Depends(get_current_entreprise),db:Session=Depends(get_db)):
    try:
        password_hash=hash_password(data.password)
        new_user = APPUserService(db).Create_user(data,entreprise_id,password_hash)
        return new_user
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=str(exc))from exc


@router.get("/me",response_model=UserResponse,status_code=200)
def get_me(current_user:APPUser=Depends(get_current_user)):
    return current_user

@router.get("",response_model=list[UserResponse],status_code=200)
def get_user_all(entreprise_id:uuid=Depends(get_current_entreprise),db:Session=Depends(get_db)):
    try:
        return APPUserService(db).get_allusers(entreprise_id)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=str(exc)) from exc


def assign_user_to_shop(shop_id:uuid,user_id:uuid=Depends(get_current_user),entreprise_id:uuid=Depends(get_current_entreprise),db:Session=Depends(get_db)):
    try:
        return APPUserService(db).assign_user_to_shop(shop_id,user_id,entreprise_id)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

@router.patch("/me",response_model=UserResponse,status_code=200)
def user_updating(data:UserUpdate,user_id:uuid,entreprise_id:uuid=Depends(get_current_entreprise),db:Session=Depends(get_db)):
    try:
        up_user=APPUserService(db).user_update(data,user_id,entreprise_id)
        return up_user
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(exc)) from exc

@router.delete("",response_model=UserResponse,status_code=200)
def user_delete(user_id:uuid,entreprise_id:uuid=Depends(get_current_entreprise),db:Session=Depends(get_db)):
    try:
        return APPUserService(db).user_delete(user_id,entreprise_id)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_200_OK,detail=str(exc)) from exc
    
    
