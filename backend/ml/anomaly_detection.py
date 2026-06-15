import pandas as pd

from sklearn.ensemble import IsolationForest

from sqlalchemy import create_engine

from config import Config

engine = create_engine(
    Config.DATABASE_URL
)


def detect_anomalies():

    query = """
    SELECT
        e.id,
        e.name,
        AVG(a.hours_worked) as avg_hours,
        AVG(p.rating) as avg_rating

    FROM employees e

    LEFT JOIN attendance a
        ON e.id = a.employee_id

    LEFT JOIN performance p
        ON e.id = p.employee_id

    GROUP BY e.id, e.name
    """

    df = pd.read_sql(
        query,
        engine
    )

    df = df.fillna(0)

    features = df[
        [
            "avg_hours",
            "avg_rating"
        ]
    ]

    model = IsolationForest(
        contamination=0.1,
        random_state=42
    )

    df["anomaly"] = model.fit_predict(
        features
    )

    results = []

    for _, row in df.iterrows():

        results.append({
            "id": int(row["id"]),
            "name": row["name"],
            "avg_hours": round(
                float(row["avg_hours"]),
                2
            ),
            "avg_rating": round(
                float(row["avg_rating"]),
                2
            ),
            "anomaly": int(row["anomaly"])
        })

    return results