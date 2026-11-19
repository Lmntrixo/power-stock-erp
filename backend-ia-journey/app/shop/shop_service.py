from app.shop.schemas import ShopResponse,ShopCreate,ShopUpdate
from app.shop.models import Shop
from app.shop.shop_repository import ShopRepository
from sqlalchemy.orm import Session
from uuid import UUID as uuid


class shopService:
    def __init__(self,db:Session):
        self.db=db
        self.repository=ShopRepository(db)

    
    def create_shops(self,data:ShopCreate,entreprise_id:uuid):
        #existing = self.repository
        shop=Shop(
            name=data.name,
            ville=data.ville,
            adresse=data.adresse,
            phone_number=data.phone_number,
            entreprise_id=entreprise_id,
            is_active=data.is_active
        )
        return self.repository.create_shop(data,entreprise_id)

    def shopby_id(self,shop_id:uuid,entreprise_id:uuid):
        shop = self.repository.get_by_id(entreprise_id,shop_id)
        if not shop:
            return "boutique introuvable"
        return shop

    def updating_shop(self,data:ShopUpdate,shop_id:uuid,entreprise_id:uuid):
        return self.repository.update_shop(data,shop_id,entreprise_id)
    
    def lists_shops(self,entreprise_id:uuid):
        return self.repository.get_all_shops(entreprise_id)

    def delete_shops(self,shop_id:uuid,entreprise_id:uuid):
        return self.repository.delete_shop(shop_id,entreprise_id)
    