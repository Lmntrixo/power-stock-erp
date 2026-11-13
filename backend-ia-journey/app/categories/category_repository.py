from sqlalchemy.orm import Session
from app.categories.models import Category

class CategoryRepostory:
    def __init__(self, db:Session):
        self.db = db

    def get_by_name(self,name:str):
        return(
            self.db.query(Category).filter(Category.name == name).first()
        )

    def add(self, category:Category):
        self.db.add(category)
        self.db.commit()
        self.db.refresh(category)
        return category
