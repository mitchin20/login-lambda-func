from sqlalchemy import Column, String, Integer, Boolean
from db.database import Base

class User(Base):
    __tablename__ = "User"

    id = Column(Integer, primary_key=True, index=True)
    firstName = Column(String(50), index=True)
    lastName = Column(String(50), index=True)
    email = Column(String(120), unique=True, index=True)
    password = Column(String)
    role = Column(String(50), index=True)
    isActive = Column(Boolean, default=True)

    def to_dict(self, exclude=None):
        exclude = exclude or []
        return {key: value for key, value in self.__dict__.items() if not key.startswith("_") and key not in exclude}