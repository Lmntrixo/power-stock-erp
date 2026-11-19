from app.core.database.connection import SessionLocal
from app.entreprise.entreprise_service import EntrepriseService
from app.entreprise.schemas import EntrepriseCreate 
from app.shop.shop_service import shopService
from app.shop.schemas import ShopCreate
from app.users.users_service import APPUserService
from app.users.schema import UserCreate
#from sqlalchemy import Session
def main():
    db = SessionLocal()
    try:
        # 1. Entreprise
        entreprise = EntrepriseService(db).create_entreprise (EntrepriseCreate(
            name="Test SARL",
            business_type="shop",
            phone_number="+237600000000",
            email="test2@example.com",
            address="Douala",
            currency="XAF",
            is_active=True
        ))
        print(f"ENTERPRISE_ID={entreprise.id}")   # ← TU COPIES CETTE LIGNE DANS .env

        # 2. Deux boutiques
        for name, ville in [("Boutique A", "Douala"), ("Boutique B", "Yaoundé")]:
            shopService(db).create_shops(
                entreprise_id=entreprise.id,   # ← passé explicitement, pas dans le body
                data=ShopCreate(name=name, ville=ville, adresse="", phone_number="", is_active=True),
            )

        # 3. Un owner (password_hash bidon — remplacé au Sprint 2)
        APPUserService(db).Create_user(
            entreprise_id=entreprise.id,
            data=UserCreate(
                name="Owner Test",
                phone="+237611111111",
                email=None,
                role="manager",
                is_active=True,
            ),
            password_hash="PENDING_SPRINT_2",   # ← placeholder explicite
        )

        db.commit()
        print("Seed OK")
    finally:
        db.close()

if __name__ == "__main__":
    main()