from flask import Blueprint, jsonify
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker

from config import Config
from models.performance import Performance
import pandas as pd

performance_bp = Blueprint(
    "performance_bp",
    __name__
)

engine = create_engine(
    Config.DATABASE_URL
)

Session = sessionmaker(bind=engine)

@performance_bp.route("/performance/stats")
def performance_stats():

    db = Session()

    avg_rating = db.query(
        func.avg(
            Performance.rating
        )
    ).scalar()

    total_reviews = db.query(
        Performance
    ).count()

    project_data = db.query(
        Performance.project,
        func.count(
            Performance.id
        )
    ).group_by(
        Performance.project
    ).all()

    projects = []

    for project, count in project_data:

        projects.append({
            "project": project,
            "count": count
        })

    db.close()

    return jsonify({
        "avg_rating": round(float(avg_rating), 2),
        "total_reviews": total_reviews,
        "projects": projects
    })

@performance_bp.route(
    "/performance",
    methods=["GET"]
)
def get_performance():

    query = """
    SELECT * FROM performance
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