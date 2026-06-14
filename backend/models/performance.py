from sqlalchemy import Column, Integer, String, Numeric
from models.base import Base

class Performance(Base):
    __tablename__ = "performance"

    id = Column(Integer, primary_key=True)

    employee_id = Column(Integer)

    rating = Column(Numeric(3,2))

    project = Column(String(100))