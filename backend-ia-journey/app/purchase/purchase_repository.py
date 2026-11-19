from app.purchase.models import Purchase, PurchaseItem
from sqlalchemy.orm import Session

class PurchaseRepository:
    def __init__(self,db:Session):
        self.db=db

    def get_by_id(self,purchase_id:int):
        return self.db.query(Purchase).filter(Purchase.id==purchase_id).first()

    def save_Purchase(self,purchase:Purchase):
        self.db.add(purchase)
        #self.db.commit()
        #self.db.refresh(purchase)  
        self.db.flush()
        return purchase      
    def save_purchase_item(self,purchase_id:int,product_id:int,quantity:int, unit_cost:int):
        db_item =PurchaseItem(
            purchase_id=purchase_id,
            product_id=product_id,
            quantity=quantity,
            unit_cost=unit_cost
        )
        self.db.add(db_item)
        return db_item