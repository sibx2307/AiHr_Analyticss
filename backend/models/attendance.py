from sqlalchemy import Column, Integer, String, Date, Numeric
from models.base import Base

class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True)

    employee_id = Column(Integer)

    date = Column(Date)

    status = Column(String(20))

    hours_worked = Column(Numeric(5,2))