from app.suppliers.models import Supplier
from app.suppliers.schemas import SupplierUpdate,SupplierCreate
from app.suppliers.supplier_repository import SupplierRepository

def Create_suppier(data:SupplierCreate,repository:SupplierRepository):
    existing_supplier = repository.get_by_email(data.email)
    if existing_supplier:
        raise ValueError("cette addresse email est deja utilise")
    supplier = Supplier(
        name=data.name,
        email=data.email,
        telephone=data.telephone,
        adresse=data.adresse,
    )
    return repository.add_supplier(supplier)
def list_allSuppliers(repository:SupplierRepository):
    all_suppliers=repository.get_all_supplier()
    return all_suppliers
def get_one_supplier_by_id(supplier_id:int,repository:SupplierRepository):
    supplier=repository.supplier_by_id(supplier_id)
    if not supplier:
        raise ValueError("ce fournisseur n'existe pas")
    return supplier