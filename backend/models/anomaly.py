from sqlalchemy import Column, Integer, Numeric, String
from models.base import Base

class Anomaly(Base):
    __tablename__ = "anomalies"

    id = Column(Integer, primary_key=True)

    employee_id = Column(Integer)

    anomaly_score = Column(Numeric(10,4))

    anomaly_status = Column(String(20))