from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from models.base import Base

class Upload(Base):

    __tablename__ = "uploads"

    id = Column(Integer, primary_key=True)

    filename = Column(String(255))

    upload_type = Column(String(50))

    uploaded_by = Column(Integer)

    uploaded_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )