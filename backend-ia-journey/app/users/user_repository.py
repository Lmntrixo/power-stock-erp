from app.users.model import APPUser
from sqlalchemy.orm import Session
from app.users.schema import UserCreate,UserUpdate
from uuid import UUID as uuid
from datetime import datetime, timezone

class AppUserRepository:
    def __init__(self,db:Session):
        self.db=db

    def get_by_id(self, user_id: uuid, entreprise_id: uuid):
        return (
            self.db.query(APPUser)
            .filter(APPUser.id == user_id)
            .filter(APPUser.entreprise_id == entreprise_id)
            .filter(APPUser.deleted_at.is_(None))
            .first()
        )
    def get_by_phone(self, phone: str, entreprise_id: uuid) -> APPUser | None:
        return (
            self.db.query(APPUser)
            .filter(APPUser.phone == phone)
            .filter(APPUser.entreprise_id == entreprise_id)
            .filter(APPUser.deleted_at.is_(None))
            .first()
        )

    def get_by_email(self,email:str,entreprise_id:uuid):
        return self.db.query(APPUser).filter(APPUser.email==email).filter(APPUser.entreprise_id==entreprise_id).filter( APPUser.deleted_at.is_(None)).first()

    def create_user(self,data:UserCreate,entreprise_id:uuid,password_hash:str):
        new_user = APPUser(
            name = data.name,
            email = data.email,
            #password_hash = data.password_hash,
            phone = data.phone,
            role = data.role,
            is_active = data.is_active,
            is_login_at = data.is_login_at,
            entreprise_id = entreprise_id,
            password_hash=password_hash
        )
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user

    def get_all_user(self,entreprise_id:uuid):
        return (
            self.db.query(APPUser).filter(APPUser.entreprise_id==entreprise_id, APPUser.deleted_at.is_(None)).all()
        )
    def delete_user(self,user_id:int,entreprise_id:uuid):
        user = self.db.query(APPUser).filter(APPUser.id==user_id, APPUser.entreprise_id==entreprise_id, APPUser.deleted_at.is_(None)).first()
        if not user:
            return None
        user.deleted_at = datetime.now(timezone.utc)
        self.db.commit()
        return user

    def update_user(self,data:UserUpdate,user_id:uuid,entreprise_id:uuid):
        user = self.db.query(APPUser).filter(APPUser.id==user_id).filter( APPUser.entreprise_id==entreprise_id).filter( APPUser.deleted_at.is_(None)).first()
        if not user:
            return None
        for key, value in data.model_dump(exclude_unset=True).items():
            setattr(user, key, value)
        self.db.commit()
        self.db.refresh(user)
        return user
    def assign_user_to_shop(self,user_id:int,shop_id:uuid,entreprise_id:uuid):
        user = self.db.query(APPUser).filter(APPUser.id==user_id, APPUser.entreprise_id==entreprise_id, APPUser.deleted_at.is_(None)).first()
        if not user:
            return None
        user.shop_id = shop_id
        self.db.commit()    

    def get_by_identifier(self,identifier:str):
        return self.db.query(APPUser).filter(
            (APPUser.email == identifier) | (APPUser.phone == identifier),
            APPUser.is_active.is_(True),
            APPUser.delete_at.is_(None)
        ).first()

    def remove_shop(self,shop_id:uuid,user_id:int,entreprise_id:uuid):
        shop_user = self.db.query(APPUser).filter(APPUser.id==user_id, APPUser.entreprise_id==entreprise_id, APPUser.shop_id==shop_id, APPUser.deleted_at.is_(None)).first()
        if not shop_user:
            return None
        shop_user.shop_id = None
        self.db.commit()
        return shop_user

    #
    def get_first_by_entreprise(self, entreprise_id: uuid)-> APPUser | None:
        #1. On part de la table AppUser
        return(
            self.db.query(APPUser)
            #2. Filtre multi-tenant: OBLIGATOIRE, sinon fuite cross-entreprise
            .filter(APPUser.entreprise_id == entreprise_id)
            #3. On ignore les soft-deleted (coherent avec deleted_at)
            .filter(APPUser.deleted_at.is_(None))
            #4.on ignore les desactives( sinon le stub pourait retourner un usractif)
            .filter(APPUser.is_active.is_(True))
            #5. Ordre deterministe : le plus ancien d'abord
            .order_by(APPUser.created_at.asc())
            #6. un seul resultat
            .first()
        )