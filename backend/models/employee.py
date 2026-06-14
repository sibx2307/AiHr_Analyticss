from sqlalchemy import Column, Integer, String, Numeric
from models.base import Base

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    department = Column(String(100))
    salary = Column(Numeric(10, 2))