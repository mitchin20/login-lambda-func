import os
import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

try:
    database_url = os.environ.get("DATABASE_URL")
except Exception as e:
    logging.error(f"Error getting DATABASE_URL: {e}")
    raise e

Base = declarative_base()

engine = create_engine(database_url, echo=True)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

# Dependency Injection for Database Session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()