from collections.abc import Generator
from sqlalchemy.orm import Session

from uuid import UUID
from fastapi import Depends, HTTPException
from app.core.database.connection import settings
from app.users.user_repository import AppUserRepository
from app.users.model import APPUser
from app.core.database.connection import SessionLocal

def get_db() -> Generator[Session,None,None]:
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

# --- STUB SPRINT 1: a remplacer au Sprint 2 ---

def get_current_entreprise()->UUID:
    """Retourne l'entre_id courant STUB: lit une variable d'env"""
    if settings.TEST_ENTERPRISE_ID is None:
        raise HTTPException(
            status_code=500,
            detail="TEST_ENTREPRISE_ID non configure dans .env  laancez scripts/sedd.py"
        )
    return settings.TEST_ENTERPRISE_ID

def get_current_user(db:Session=Depends(get_db))-> APPUser:
    entreprise_id = get_current_entreprise()
    user = AppUserRepository(db).get_first_by_entreprise(entreprise_id)
    if user is None:
        #cas de demarrage: le seed n'a pas lance, ou TEST_ENTERPRISE_ID est faux
        raise HTTPException(
            status_code=500,
            detail="sub get_current_user: aucun utilisateur trouve pour TEST_ENTREPRISE_ID avez-vous lance scropts/seed.py"
        )
    return user
    """Retourne l'utilisateur courant. STUB: prend le premier user de l'entreprise"""
   # return AppUserRepository(db).get_first_entreprise(get_current_entreprise())
