import pandas as pd


def validate_csv(df, required_columns):
    errors = []

    # Check missing columns
    missing = set(required_columns) - set(df.columns)

    if missing:
        errors.append(
            f"Missing columns: {list(missing)}"
        )

    # Check empty values
    if df.isnull().sum().sum() > 0:
        errors.append(
            "Dataset contains empty values"
        )

    return errors