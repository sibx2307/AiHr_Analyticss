from flask import Flask
from flask_cors import CORS

from flask_jwt_extended import JWTManager

from routes.auth_routes import auth_bp

from routes.employee_routes import employee_bp
from routes.attendance_routes import attendance_bp
from routes.performance_routes import performance_bp
from routes.anomaly_routes import anomaly_bp

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "super-secret-key"

jwt = JWTManager(app)

CORS(app)

app.register_blueprint(auth_bp)

app.register_blueprint(employee_bp)

app.register_blueprint(attendance_bp)

app.register_blueprint(performance_bp)

app.register_blueprint(anomaly_bp)


@app.route("/")
def home():
    return {
        "status": "success",
        "message": "AI HR Analytics API Running",
        "version": "1.0"
    }

@app.route("/health")
def health():
    return {
        "status": "healthy"
    }

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )