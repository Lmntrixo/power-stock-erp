from fastapi import FastAPI, HTTPException,Depends
from typing import Annotated
from sqlalchemy.orm import Session
from sqlalchemy import text

from fastapi.middleware.cors import CORSMiddleware
from app.core.database.connection import engine
from app.core.database.dependancies import get_db
from app.core.database.connection import Base
from app.customers.models import Customer
from app.categories.models import Category
from app.products.models import Product
from app.categories.categorie_routes import router as category_router
from app.customers.customer_routes import router as customer_router
from app.products.product_routes import router as product_router
from app.suppliers.suplier_routes import router as supplier_router
from app.purchase.purchae_routes import router as purchase_router
from app.shop.shop_routes import router as  shop_router
from app.entreprise.entreprise_routes import router as entreprise_router
from app.users.users_routes import router as users_router
DbSession = Annotated[Session, Depends(get_db)]
app = FastAPI(title="backend Engineering project")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/heal")
def health_check():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
            return {
                "status":"healthy",
                "database": "connected"
            }
    except Exception:
        return {
            "status":"unhealthy",
            "database":"disconnected"
        }

@app.get("/customer")
def get_customers(db: DbSession):
    #
    return {
        "message":"Session disponible"
    }
app.include_router(customer_router)
app.include_router(category_router)
app.include_router(product_router)
app.include_router(supplier_router)
app.include_router(purchase_router)
app.include_router(shop_router)
app.include_router(entreprise_router)
app.include_router(users_router)