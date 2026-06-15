from flask import Blueprint
from flask import jsonify

from ml.anomaly_detection import (
    detect_anomalies
)

anomaly_bp = Blueprint(
    "anomaly_bp",
    __name__
)


@anomaly_bp.route("/anomalies")
def get_anomalies():

    results = detect_anomalies()

    return jsonify(results)