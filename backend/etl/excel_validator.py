import pandas as pd


def validate_excel(file_path, required_columns):

    df = pd.read_excel(file_path)

    missing = set(required_columns) - set(df.columns)

    if missing:
        return [f"Missing columns: {list(missing)}"]

    return []