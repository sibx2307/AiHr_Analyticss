from flask import Blueprint
from flask import request
from flask import jsonify

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import Config

from models.user import User

import bcrypt

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