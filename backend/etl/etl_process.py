
import pandas as pd

from sqlalchemy import create_engine

from config import Config

from etl.csv_validator import validate_csv


engine = create_engine(
    Config.DATABASE_URL
)

# ----------------------
# Employees
# ----------------------

employees = pd.read_csv(
    "../data/employees.csv"
)

errors = validate_csv(
    employees,
    ["id", "name", "department", "salary"]
)

if errors:
    print(errors)
else:
    employees.to_sql(
        "employees",
        engine,
        if_exists="append",
        index=False
    )

    print("Employees loaded")

# ----------------------
# Attendance
# ----------------------

attendance = pd.read_csv(
    "../data/attendance.csv"
)

errors = validate_csv(
    attendance,
    [
        "employee_id",
        "date",
        "status",
        "hours_worked"
    ]
)

if errors:
    print(errors)

else:

    attendance.to_sql(
        "attendance",
        engine,
        if_exists="append",
        index=False
    )

    print("Attendance loaded")

# ----------------------
# Performance
# ----------------------

performance = pd.read_csv(
    "../data/performance.csv"
)

errors = validate_csv(
    performance,
    [
        "employee_id",
        "rating",
        "project"
    ]
)

if errors:
    print(errors)

else:

    performance.to_sql(
        "performance",
        engine,
        if_exists="append",
        index=False
    )

    print("Performance loaded")

print("ETL completed")