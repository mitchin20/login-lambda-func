from sqlalchemy.orm import Session
from models.user_model import User
from utils.verify_password import verify_password

def get_user(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()
    
    if not user and not verify_password(password, user.password):
        return None

    dict_user = user.to_dict(exclude=["password"])

    return dict_user if dict_user else None