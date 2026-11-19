from app.entreprise.models import Entreprise
from app.entreprise.schemas import EntrepriseCreate,EntrepriseUpdate
from uuid import UUID as uuid
from datetime import datetime,timezone

class EntrepriseRepository:
    def __init__(self,db):
        self.db = db

    def get_by_email(self,email:str):
        return (
            self.db.query(Entreprise).filter(Entreprise.deleted_at.is_(None)).filter(Entreprise.email==email).first()
        )

    def create_entreprises(self,data:EntrepriseCreate):
        entreprise = Entreprise(
            name=data.name,
            address=data.address,
            email=data.email,
            phone_number=data.phone_number,
            business_type=data.business_type,
            currency=data.currency,
            is_active=data.is_active
        )
        self.db.add(entreprise)
        self.db.commit()
        self.db.refresh(entreprise)
        return entreprise


    def get_all_entreprises(self):
        return (
            self.db.query(Entreprise).filter(Entreprise.deleted_at.is_(None)).all()
        )
    def get_entreprise_by_id(self,entreprise_id:uuid):
        return (
            self.db.query(Entreprise).filter(Entreprise.deleted_at.is_(None)).filter(Entreprise.id==entreprise_id).first()
        )
    def delete_entreprise(self,entreprise_id:uuid):
        entreprise = self.db.query(Entreprise).filter(Entreprise.id==entreprise_id).first()
        if not entreprise:
            return None
        entreprise.deleted_at = datetime.now(timezone.utc)
        self.db.commit()

        return entreprise

    
    