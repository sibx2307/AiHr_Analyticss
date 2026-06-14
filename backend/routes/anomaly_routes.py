from flask import Blueprint, jsonify
from sqlalchemy import create_engine
from config import Config
import pandas as pd

anomaly_bp = Blueprint(
    "anomaly_bp",
    __name__
)

engine = create_engine(
    Config.DATABASE_URL
)

@anomaly_bp.route(
    "/anomalies",
    methods=["GET"]
)
def get_anomalies():

    query = """
    SELECT * FROM anomalies
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