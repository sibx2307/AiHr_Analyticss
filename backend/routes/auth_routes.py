from flask import Blueprint
from flask import request
from flask import jsonify

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import Config

from models.user import User

import bcrypt
from flask_jwt_extended import create_access_token



auth_bp = Blueprint(
    "auth_bp",
    __name__
)

engine = create_engine(
    Config.DATABASE_URL
)

Session = sessionmaker(
    bind=engine
)


auth_bp = Blueprint(
    "auth_bp",
    __name__
)

engine = create_engine(
    Config.DATABASE_URL
)

Session = sessionmaker(
    bind=engine
)


@auth_bp.route("/register", methods=["POST"])
def register():

    data = request.get_json()

    username = data.get("username")
    email = data.get("email")
    password = data.get("password")
    role = data.get("role", "Employee")

    db = Session()

    existing_user = db.query(User).filter(
        User.username == username
    ).first()

    if existing_user:
        db.close()
        return jsonify({
            "message": "User already exists"
        }), 400

    password_hash = bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    ).decode("utf-8")

    new_user = User(
        username=username,
        email=email,
        password_hash=password_hash,
        role=role
    )

    db.add(new_user)
    db.commit()
    db.close()

    return jsonify({
        "message": "User registered successfully"
    })



@auth_bp.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    db = Session()

    user = db.query(User).filter(
        User.username == username
    ).first()

    db.close()

    if not user:
        return jsonify({
            "message": "Invalid username or password"
        }), 401

    if not bcrypt.checkpw(
        password.encode("utf-8"),
        user.password_hash.encode("utf-8")
    ):
        return jsonify({
            "message": "Invalid username or password"
        }), 401

    access_token = create_access_token(
        identity=username
    )

    return jsonify({
        "access_token": access_token,
        "username": user.username,
        "role": user.role
    }), 200