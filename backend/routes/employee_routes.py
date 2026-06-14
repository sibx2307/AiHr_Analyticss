from flask import Blueprint, jsonify
from sqlalchemy import create_engine
from config import Config
import pandas as pd

employee_bp = Blueprint(
    "employee_bp",
    __name__
)

engine = create_engine(
    Config.DATABASE_URL
)

@employee_bp.route(
    "/employees",
    methods=["GET"]
)
def get_employees():

    query = """
    SELECT * FROM employees
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