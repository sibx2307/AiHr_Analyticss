import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

import pandas as pd

from sklearn.ensemble import IsolationForest

from sqlalchemy import create_engine

from config import Config

engine = create_engine(Config.DATABASE_URL)

# ----------------------------------
# Load Data
# ----------------------------------

attendance = pd.read_sql(
    "SELECT * FROM attendance",
    engine
)

performance = pd.read_sql(
    "SELECT * FROM performance",
    engine
)

# ----------------------------------
# Merge Data
# ----------------------------------

merged = pd.merge(
    attendance,
    performance,
    on="employee_id",
    how="inner"
)

# ----------------------------------
# Features
# ----------------------------------

features = merged[
    [
        "hours_worked",
        "rating"
    ]
]

# ----------------------------------
# Isolation Forest
# ----------------------------------

model = IsolationForest(
    contamination=0.1,
    random_state=42
)

merged["prediction"] = model.fit_predict(
    features
)

merged["anomaly_score"] = model.decision_function(
    features
)

# ----------------------------------
# Store Results
# ----------------------------------

results = merged[
    [
        "employee_id",
        "anomaly_score",
        "prediction"
    ]
]

results["anomaly_status"] = results[
    "prediction"
].apply(
    lambda x: "Anomaly"
    if x == -1
    else "Normal"
)

results = results[
    [
        "employee_id",
        "anomaly_score",
        "anomaly_status"
    ]
]

results.to_sql(
    "anomalies",
    engine,
    if_exists="replace",
    index=False
)

print(
    "\nAnomaly Detection Complete!"
)

print(
    results.head()
)