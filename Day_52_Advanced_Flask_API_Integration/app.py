from flask import Flask, jsonify  # type: ignore[import-not-found]

from auth.routes import auth_bp
from students.routes import students_bp

app = Flask(__name__)
app.secret_key = "day52-secret-key"

app.register_blueprint(auth_bp)
app.register_blueprint(students_bp)


@app.route("/")
def home():
    return jsonify({
        "message": "Day 52 Advanced Flask API is running"
    })


@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": "Resource not found"
    }), 404


@app.errorhandler(500)
def server_error(error):
    return jsonify({
        "success": False,
        "error": "Internal server error"
    }), 500


if __name__ == "__main__":
    app.run(debug=True)