from flask import Blueprint, jsonify
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker

from config import Config

from models.employee import Employee
from models.attendance import Attendance
from models.performance import Performance

dashboard_bp = Blueprint(
    "dashboard_bp",
    __name__
)

engine = create_engine(
    Config.DATABASE_URL
)

Session = sessionmaker(
    bind=engine
)


@dashboard_bp.route("/dashboard/stats")
def dashboard_stats():

    db = Session()

    total_employees = db.query(
        Employee
    ).count()

    total_attendance = db.query(
        Attendance
    ).count()

    present_count = db.query(
        Attendance
    ).filter(
        Attendance.status == "Present"
    ).count()

    attendance_percentage = 0

    if total_attendance > 0:
        attendance_percentage = round(
            (present_count / total_attendance) * 100,
            2
        )

    avg_rating = db.query(
        func.avg(
            Performance.rating
        )
    ).scalar()

    if avg_rating:
        avg_rating = round(
            float(avg_rating),
            2
        )
    else:
        avg_rating = 0

    db.close()

    return jsonify({
        "employees": total_employees,
        "attendance": attendance_percentage,
        "performance": avg_rating,
        "anomalies": 0
    })