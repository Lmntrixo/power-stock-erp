from fastapi import APIRouter,Depends,HTTPException,Header,status
from app.core.database.dependancies import get_db,get_current_entreprise
from app.shop.models import Shop
from app.shop.schemas import ShopCreate,ShopResponse,ShopUpdate
from app.shop.shop_service import shopService
from sqlalchemy.orm import Session
from uuid import UUID as uuid

router = APIRouter(prefix="/shops",tags=["shops"])
#creer une boutique
@router.post("",response_model=ShopResponse,status_code=201)
def creating_shop(data:ShopCreate,entreprise_id:uuid=Depends(get_current_entreprise),db:Session=Depends(get_db)):
    try:
        shop= shopService(db).create_shops(data,entreprise_id)
        return shop
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=str(exc)) from exc

@router.get("/{shop_id}",response_model=ShopResponse,status_code=200)
def shop_byid(shop_id:uuid,entreprise_id:uuid=Depends(get_current_entreprise),db:Session=Depends(get_db)):
    try:
        shop=shopService(db).shopby_id(entreprise_id,shop_id)
        return shop
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=str(exc)) from exc

@router.get("",response_model=list[ShopResponse],status_code=200)
def get_shop_all(entreprise_id:uuid=Depends(get_current_entreprise),db:Session=Depends(get_db)):
    try:
        all_shop= shopService(db).lists_shops(entreprise_id)
        return all_shop
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=str(exc)) from exc

@router.patch("/{shop_id}",response_model=ShopResponse,status_code=201)
def updating_shop(data:ShopUpdate,shop_id:uuid,entreprise_id:uuid=Depends(get_current_entreprise),db:Session=Depends(get_db)):
    try:
        up_shop=shopService(db).updating_shop(data,shop_id,entreprise_id)
        if up_shop is None:                                            # ← LA ligne qui manque
                 raise HTTPException(status_code=404, detail="Boutique introuvable")
        return up_shop
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=str(exc)) from exc


@router.delete("",response_model=ShopResponse,status_code=200)
def delteting_shop(shop_id:uuid,entreprise_id:uuid=Depends(get_current_entreprise),db:Session=Depends(get_db)):
    try:
        del_shop = shopService(db).delete_shops(shop_id,entreprise_id)
        return del_shop
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc