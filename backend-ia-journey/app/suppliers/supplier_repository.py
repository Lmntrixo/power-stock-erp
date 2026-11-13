from sqlalchemy.orm import Session 
from app.suppliers.models import Supplier

class SupplierRepository:
    def __init__(self,db:Session):
        self.db = db

    def get_by_email(self,email:str):
        return (
            self.db.query(Supplier).filter(Supplier.email==email).first()
        )
    def add_supplier(self, suplier: Supplier):
        self.db.add(suplier)
        self.db.commit()
        self.db.refresh(suplier)
        return suplier
    def get_all_supplier(self):
        return(
            self.db.query(Supplier).all()
        )
    def supplier_by_id(self,supplier_id:int):
        return(
            self.db.query(Supplier).filter(Supplier.id==supplier_id).first()
        )