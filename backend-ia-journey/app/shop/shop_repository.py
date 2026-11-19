from app.shop.models import Shop
from sqlalchemy.orm import Session
from app.shop.schemas import ShopCreate,ShopUpdate
from uuid import UUID as uuid

class ShopRepository:
    def __init__(self,db:Session):
        self.db=db

    def get_by_id(self,shop_id:uuid,entreprise_id:uuid,):
        return (
            self.db.query(Shop).filter(Shop.id==shop_id,Shop.entreprise_id==entreprise_id).first()

        ) 
    def get_all_shops(self,entreprise_id:uuid):
        return (
            self.db.query(Shop).filter(Shop.entreprise_id==entreprise_id).all()
        )
    def create_shop(self,data:ShopCreate,entreprise_id:uuid):
        new_shop = Shop(
            name = data.name,
            ville = data.ville,
            entreprise_id = entreprise_id,
            adresse = data.adresse,
            phone_number =data.phone_number,
            is_active = data.is_active
        )
        self.db.add(new_shop)
        self.db.commit()
        self.db.refresh(new_shop)
        return new_shop
    
    def update_shop(self,data:ShopUpdate,shop_id:uuid,entreprise_id:uuid):
        shop = self.db.query(Shop).filter(Shop.entreprise_id==entreprise_id).filter(Shop.id==shop_id).first()
        if not shop:
            return None
        for key, value in data.model_dump(exclude_unset=True).items():
            setattr(shop, key, value)
            self.db.commit()
            self.db.refresh(shop)
        return shop

    def delete_shop(self,shop_id:uuid,entreprise_id:uuid):
        shop= self.db.query(Shop).filter(Shop.entreprise_id==entreprise_id).filter(Shop.id==shop_id).first()
        self.db.delete(shop)
        self.db.commit()
        self.db.refresh(shop)