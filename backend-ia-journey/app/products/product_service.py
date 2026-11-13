from app.products.product_repository import ProductRepsitory
from app.products.schema import ProductCreate
from app.products.models import Product

def create_Product(data:ProductCreate,repository:ProductRepsitory):
    existing_product = repository.get_by_sku(data.sku)
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
    return repository.add(product)

def get_all_products(repository:ProductRepsitory):
    return repository.get_all_product()