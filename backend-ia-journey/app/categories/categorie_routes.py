from fastapi import APIRouter,HTTPException,status,Depends
from sqlalchemy.orm import Session
from app.categories.schema import CategoryCreate,CategoryResponse
from app.categories.category_repository import CategoryRepostory
from app.categories import models
from app.categories.category_service import create_category
from app.core.database.dependancies import get_db

router  = APIRouter(prefix="/categories", tags=["Categories"])

@router.post("", response_model=CategoryResponse, status_code=201)
def create_category_route(data:CategoryCreate, db:Session=Depends(get_db)):
    repository = CategoryRepostory(db)
    try:
        category = create_category(data,repository)
        return category
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=str(exc)) from exc