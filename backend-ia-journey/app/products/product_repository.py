from sqlalchemy.orm import Session
from app.products.models import Product

class ProductRepsitory:
    def __init__(self, db:Session):
        self.db = db

    def get_by_sku(self, sku:str):
        return(
            self.db.query(Product).filter(Product.sku == sku).first()
        )
    def get_by_id(self,product_id:int):
        return( self.db.query(Product).filter(Product.id==product_id).first())
    def get_all_product(self):
        return(
            self.db.query(Product).all()
        )
    def add(self, product:Product):
        self.db.add(product)
        self.db.commit()
        self.db.refresh(product)
        return product

    def increment_stock(self,product:Product,quantity:int):
        product.stock_quantity +=quantity
