from flask import Blueprint
from flask import request
from flask import jsonify

from sqlalchemy import create_engine

from config import Config

import pandas as pd

upload_bp = Blueprint(
    "upload_bp",
    __name__
)

engine = create_engine(
    Config.DATABASE_URL
)


@upload_bp.route(
    "/upload/employees",
    methods=["POST"]
)
def upload_employees():

    if "file" not in request.files:

        return jsonify({
            "message":
            "No file uploaded"
        }), 400

    file = request.files["file"]

    df = pd.read_csv(file)

    df.to_sql(
        "employees",
        engine,
        if_exists="append",
        index=False
    )

    return jsonify({
        "message":
        "Employees uploaded successfully"
    })