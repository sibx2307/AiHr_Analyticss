from flask import Blueprint, jsonify
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from config import Config
from models.attendance import Attendance
import pandas as pd

attendance_bp = Blueprint(
    "attendance_bp",
    __name__
)

engine = create_engine(
    Config.DATABASE_URL
)

Session = sessionmaker(
    bind=engine
)

@attendance_bp.route(
    "/attendance",
    methods=["GET"]
)
def get_attendance():

    query = """
    SELECT * FROM attendance
    """

    df = pd.read_sql(
        query,
        engine
    )

    return jsonify(
        df.to_dict(
            orient="records"
        )
    )

@attendance_bp.route("/attendance/stats")
def attendance_stats():

    db = Session()

    present = db.query(
        Attendance
    ).filter(
        Attendance.status == "Present"
    ).count()

    absent = db.query(
        Attendance
    ).filter(
        Attendance.status == "Absent"
    ).count()

    avg_hours = db.query(
        func.avg(
            Attendance.hours_worked
        )
    ).scalar()

    db.close()

    return jsonify({
        "present": present,
        "absent": absent,
        "avg_hours": round(float(avg_hours), 2)
    })