from app.entreprise.models import Entreprise
from app.entreprise.schemas import EntrepriseCreate,EntrepriseUpdate
from app.entreprise.entreprise_repository import EntrepriseRepository
from sqlalchemy.orm import Session
from fastapi import HTTPException,status
from app.shop.schemas import ShopCreate
from app.shop.models import Shop
from app.shop.shop_repository import ShopRepository
from uuid import UUID as uuid       


class EntrepriseService:
    def __init__ (self, db:Session):
        self.db = db
        self.repository = EntrepriseRepository(db)
        self.db.shop_repository = ShopRepository(db)
     

    def create_entreprise(self,data:EntrepriseCreate):
        existing_entreprise = self.repository.get_by_email(data.email)
        if existing_entreprise:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail="Entreprise with this email already exists"
    )
        product = Entreprise(
            name=data.name,
            email=data.email,
            phone_number=data.phone_number,
            address=data.address,
            business_type=data.business_type,
            currency=data.currency,
            is_active=data.is_active
        )
        return self.repository.create_entreprises(product)
    
    def list_all_entreprise(self):
        entreprise = self.repository.get_all_entreprises()
        if not entreprise:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No entreprise found")
        return entreprise
    def updating_entreprise(self,data:EntrepriseUpdate,entreprise_id:uuid):
        entreprise = self.repository.get_entreprise_by_id(entreprise_id)
        if not entreprise:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="entreprise introuvable")
        update_entreprise= Entreprise(
            name=data.name,
            address=data.address,
            email=data.email,
            business_type=data.business_type,
            currency=data.currency,
            is_active=data.is_active
        )
        return self.repository.update_entreprise(data,entreprise_id)

    def delete_an_enreprise(self,entreprise_id:uuid):
        soft_delete= self.repository.delete_entreprise(entreprise_id)    
        if not soft_delete:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return soft_delete
            