from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from models.base import Base

class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)

    username = Column(String(100), unique=True)

    email = Column(String(255))

    password_hash = Column(String)

    role = Column(String(50))

    created_at = Column(DateTime(timezone=True),
                        server_default=func.now())