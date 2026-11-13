from sqlalchemy.orm import Session
from app.customers.models import Customer

class CustomerRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_by_email(self, email: str):
        return (
            self.db.query(Customer).filter(Customer.email == email).first()
        )
    def get_by_id(self,customer_id:int):
        return(
            self.db.query(Customer).filter(Customer.id == customer_id).first()
        )
    def get_all_customers(self):
        return (
            self.db.query(Customer).all()
        )
    def add(self, customer:Customer):
        self.db.add(customer)
        self.db.commit()
        self.db.refresh(customer)
        return customer
    