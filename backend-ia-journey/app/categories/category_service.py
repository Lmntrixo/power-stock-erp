from app.categories.category_repository import CategoryRepostory
from app.categories.schema import CategoryCreate
from app.categories.models import Category

def create_category(data:CategoryCreate, repository: CategoryRepostory):
    existing_category = repository.get_by_name(data.name)
    if existing_category:
        raise ValueError( "cette categorie existe deja")
    categorie = Category(
        name=data.name,
        description=data.description,   
    )
    return repository.add(categorie)