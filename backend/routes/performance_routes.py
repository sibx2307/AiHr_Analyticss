from flask import Blueprint, jsonify
from sqlalchemy import create_engine
from config import Config
import pandas as pd

performance_bp = Blueprint(
    "performance_bp",
    __name__
)

engine = create_engine(
    Config.DATABASE_URL
)

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