from sqlalchemy.orm import Session
from app.users.model import APPUser
from app.users.schema import UserCreate,UserUpdate
from app.users.user_repository import AppUserRepository
from app.shop.shop_repository import ShopRepository
from uuid import UUID as uuid
from fastapi import HTTPException,status

class APPUserService:
    def __init__(self,db:Session):
        self.db=db
        self.repository=AppUserRepository(db)
        self.shop_repo=ShopRepository(db)

    def Create_user(self, data:UserCreate,entreprise_id:uuid,password_hash:str):
        #verifie si l'utilisateur n'existe pas
        existing_user = self.repository.get_by_email(data.email,entreprise_id)
        #if data.email is None:
         #   raise ValueError("veuillez remplir votre email")
        if existing_user:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail="utilisateur existe deja")
        
        app_user= APPUser(
            name=data.name,
            email=data.email,
            phone=data.phone,
            role=data.role,
            is_active=data.is_active,
            password_hash=password_hash,
            entreprise_id=entreprise_id

        )
        return self.repository.create_user(app_user,entreprise_id,password_hash)
    
    def assign_user_to_shop(self,user_id:int,shop_id:uuid,entreprise_id:uuid):
        user_existing=self.repository.get_by_id(user_id,entreprise_id)
        shop_existing=self.shop_repo.get_by_id(shop_id,entreprise_id)

        if user_existing | shop_existing is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="aucune occurence")

        return self.repository.assign_user_to_shop(user_id,shop_id,entreprise_id)
    
    def get_user_byid(self,user_id:uuid):
        users= self.repository.get_by_id(user_id)
        if users is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="aucun utilisateur")
        return users
    def get_allusers(self,entreprise_id:uuid):
        return self.repository.get_all_user(entreprise_id)

    def user_update(self,data:UserUpdate,user_id:uuid, entreprise_id:uuid):
        up_user = self.repository.update_user(data,user_id,entreprise_id)
        if up_user is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="utilisateur introuvable")
        return up_user
    
    def user_delete(self,user_id:uuid,entreprise_id:uuid):
        return self.repository.delete_user(user_id,entreprise_id)