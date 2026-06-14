from db_connection import engine
from models.base import Base

# Import all models

from models.employee import Employee
from models.attendance import Attendance
from models.performance import Performance
from models.anomaly import Anomaly
from models.user import User
from models.upload import Upload

Base.metadata.create_all(bind=engine)

print("All tables created successfully!")