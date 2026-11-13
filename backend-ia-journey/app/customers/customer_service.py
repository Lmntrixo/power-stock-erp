from app.customers.customer_repository import CustomerRepository
from app.customers.schema import CustomerCreate
from app.customers.models import Customer

def create_customer(data:CustomerCreate,repository: CustomerRepository):
    existing_customer = repository.get_by_email(data.email)
    if existing_customer:
        raise ValueError ("cette adresse email est deja utilisee")

    customer = Customer(
        name=data.name,
        email=data.email,
        phone=data.phone
    )
    return repository.add(customer)

def list_customers(repository:CustomerRepository):
    return repository.get_all_customers()

def get_customer_by_id(customer_id:int, repository:CustomerRepository):
    customer = repository.get_by_id(customer_id)
    if not customer:
        raise ValueError("Customer not found")
    return customer