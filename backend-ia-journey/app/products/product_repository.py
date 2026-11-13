from sqlalchemy.orm import Session
from app.products.models import Product

class ProductRepsitory:
    def __init__(self, db:Session):
        self.db = db

    def get_by_sku(self, sku:str):
        return(
            self.db.query(Product).filter(Product.sku == sku).first()
        )
    def get_all_product(self):
        return(
            self.db.query(Product).all()
        )
    def add(self, product:Product):
        self.db.add(product)
        self.db.commit()
        self.db.refresh(product)
        return product