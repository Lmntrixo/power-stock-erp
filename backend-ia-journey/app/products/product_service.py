from app.products.product_repository import ProductRepsitory
from app.products.schema import ProductCreate
from app.products.models import Product
from sqlalchemy.orm import Session

class ProductService:
    def __init__(self,db:Session,repository:ProductRepsitory):
        self.db=db
        self.repository=repository        

    def create_Product(self,data:ProductCreate):
        existing_product = self.repository.get_by_sku(data.sku)
        if existing_product:
            raise ValueError(" un produit avec ce sku est deja cree en base donnees ")
        product = Product(
            name=data.name,
            description=data.description,
            sku=data.sku,
            unit_price=data.unit_price,
            stock_quantity=data.stock_quantity,
            categorie_id=data.categorie_id


        ) 
        return self.repository.add(product)

    def get_all_products(self)->list[Product]:
        return self.repository.get_all_product()