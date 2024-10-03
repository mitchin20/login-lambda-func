import logging
from sqlalchemy.orm import Session

def db_session(get_db_func):
    try:
        db: Session = next(get_db_func())
        return db
    except Exception as e:
        logging.error(f"Failed to create DB session: {e}")
        return None