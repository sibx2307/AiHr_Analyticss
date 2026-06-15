from flask import Blueprint, request, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import Config
from models.employee import Employee

employee_bp = Blueprint(
    "employee_bp",
    __name__
)

engine = create_engine(
    Config.DATABASE_URL
)

Session = sessionmaker(
    bind=engine
)


# GET ALL EMPLOYEES
@employee_bp.route("/employees", methods=["GET"])
def get_employees():

    db = Session()

    employees = db.query(Employee).all()

    results = []

    for emp in employees:

        results.append({
            "id": emp.id,
            "name": emp.name,
            "department": emp.department,
            "salary": float(emp.salary)
        })

    db.close()

    return jsonify(results)


# GET SINGLE EMPLOYEE
@employee_bp.route("/employees/<int:id>", methods=["GET"])
def get_employee(id):

    db = Session()

    emp = db.query(Employee).filter(
        Employee.id == id
    ).first()

    db.close()

    if not emp:
        return jsonify({
            "message": "Employee not found"
        }), 404

    return jsonify({
        "id": emp.id,
        "name": emp.name,
        "department": emp.department,
        "salary": float(emp.salary)
    })


# CREATE EMPLOYEE
@employee_bp.route("/employees", methods=["POST"])
def create_employee():

    data = request.get_json()

    db = Session()

    employee = Employee(
        name=data["name"],
        department=data["department"],
        salary=data["salary"]
    )

    db.add(employee)
    db.commit()

    db.close()

    return jsonify({
        "message": "Employee created successfully"
    })

@employee_bp.route("/employees/<int:id>", methods=["DELETE"])
def delete_employee(id):

    db = Session()

    employee = db.query(Employee).filter(
        Employee.id == id
    ).first()

    if not employee:
        db.close()
        return jsonify({
            "message": "Employee not found"
        }), 404

    db.delete(employee)
    db.commit()
    db.close()

    return jsonify({
        "message": "Employee deleted"
    })

@employee_bp.route("/employees/<int:id>", methods=["PUT"])
def update_employee(id):

    data = request.get_json()

    db = Session()

    employee = db.query(Employee).filter(
        Employee.id == id
    ).first()

    if not employee:
        db.close()
        return jsonify({
            "message": "Employee not found"
        }), 404

    employee.name = data["name"]
    employee.department = data["department"]
    employee.salary = data["salary"]

    db.commit()
    db.close()

    return jsonify({
        "message": "Employee updated successfully"
    })