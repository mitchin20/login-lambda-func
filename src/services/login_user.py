from sqlalchemy.orm import Session
from services.get_user_service import get_user

def login(db: Session, email: str, password: str):
    return get_user(db, email, password)