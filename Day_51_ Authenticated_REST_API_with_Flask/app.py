from flask import (
    Flask,
    request,
    jsonify,
    render_template,
    redirect,
    url_for,
    session
)

import sqlite3

from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)


# ==========================================
# FLASK APPLICATION
# ==========================================

app = Flask(__name__)

# Secret key for session management
app.secret_key = "day51-secret-key-change-later"


# Database
DATABASE = "database.db"


# ==========================================
# DATABASE CONNECTION
# ==========================================

def get_db_connection():

    conn = sqlite3.connect(DATABASE)

    conn.row_factory = sqlite3.Row

    return conn


# ==========================================
# AUTHENTICATION HELPER
# ==========================================

def is_authenticated():

    return "user_id" in session


# ==========================================
# HOME
# ==========================================

@app.route("/")
def home():

    if is_authenticated():

        return redirect(url_for("dashboard"))

    return redirect(url_for("login"))


# ==========================================
# REGISTER
# ==========================================

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        # Validation
        if not username or not password:

            return "Username and password are required", 400

        if len(username) < 3:

            return "Username must contain at least 3 characters", 400

        if len(password) < 6:

            return "Password must contain at least 6 characters", 400

        conn = get_db_connection()

        try:

            password_hash = generate_password_hash(password)

            conn.execute(
                """
                INSERT INTO users (username, password)
                VALUES (?, ?)
                """,
                (username, password_hash)
            )

            conn.commit()

        except sqlite3.IntegrityError:

            conn.close()

            return "Username already exists", 409

        conn.close()

        return redirect(url_for("login"))

    return render_template("register.html")


# ==========================================
# LOGIN
# ==========================================

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        # Validation
        if not username or not password:

            if request.is_json:

                return jsonify({
                    "error": "Username and password are required"
                }), 400

            return "Username and password are required", 400

        conn = get_db_connection()

        user = conn.execute(
            """
            SELECT id, username, password
            FROM users
            WHERE username = ?
            """,
            (username,)
        ).fetchone()

        conn.close()

        # User doesn't exist
        if user is None:

            if request.is_json:

                return jsonify({
                    "error": "Invalid username or password"
                }), 401

            return "Invalid username or password", 401

        # Check password
        if not check_password_hash(user["password"], password):

            if request.is_json:

                return jsonify({
                    "error": "Invalid username or password"
                }), 401

            return "Invalid username or password", 401

        # --------------------------
        # LOGIN SUCCESSFUL
        # --------------------------

        session.clear()

        session["user_id"] = user["id"]
        session["username"] = user["username"]

        # If Postman/API sends JSON
        if request.is_json:

            return jsonify({
                "message": "Login successful",
                "username": user["username"]
            }), 200

        # Browser
        return redirect(url_for("dashboard"))

    return render_template("login.html")


# ==========================================
# LOGOUT
# ==========================================

@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("login"))


# ==========================================
# DASHBOARD
# ==========================================

@app.route("/dashboard")
def dashboard():

    if not is_authenticated():

        return redirect(url_for("login"))

    conn = get_db_connection()

    students = conn.execute(
        """
        SELECT id, name, marks
        FROM students
        ORDER BY id
        """
    ).fetchall()

    conn.close()

    return render_template(
        "dashboard.html",
        username=session["username"],
        students=students
    )


# ==========================================
# API AUTHENTICATION CHECK
# ==========================================

def api_auth_required():

    if "user_id" not in session:

        return jsonify({
            "error": "Authentication required"
        }), 401

    return None


# ==========================================
# GET ALL STUDENTS
# ==========================================

@app.route("/api/students", methods=["GET"])
def get_students():

    auth_error = api_auth_required()

    if auth_error:

        return auth_error

    conn = get_db_connection()

    students = conn.execute(
        """
        SELECT id, name, marks
        FROM students
        ORDER BY id
        """
    ).fetchall()

    conn.close()

    result = []

    for student in students:

        result.append({
            "id": student["id"],
            "name": student["name"],
            "marks": student["marks"]
        })

    return jsonify(result), 200


# ==========================================
# GET ONE STUDENT
# ==========================================

@app.route("/api/students/<int:student_id>", methods=["GET"])
def get_student(student_id):

    auth_error = api_auth_required()

    if auth_error:

        return auth_error

    conn = get_db_connection()

    student = conn.execute(
        """
        SELECT id, name, marks
        FROM students
        WHERE id = ?
        """,
        (student_id,)
    ).fetchone()

    conn.close()

    if student is None:

        return jsonify({
            "error": "Student not found"
        }), 404

    return jsonify({
        "id": student["id"],
        "name": student["name"],
        "marks": student["marks"]
    }), 200


# ==========================================
# CREATE STUDENT
# ==========================================

@app.route("/api/students", methods=["POST"])
def create_student():

    auth_error = api_auth_required()

    if auth_error:

        return auth_error

    data = request.get_json(silent=True)

    if not data:

        return jsonify({
            "error": "JSON body is required"
        }), 400

    name = str(data.get("name", "")).strip()
    marks = data.get("marks")

    # Name validation
    if not name:

        return jsonify({
            "error": "Name is required"
        }), 400

    # Marks validation
    if marks is None:

        return jsonify({
            "error": "Marks are required"
        }), 400

    try:

        marks = int(marks)

    except (ValueError, TypeError):

        return jsonify({
            "error": "Marks must be a number"
        }), 400

    if not 0 <= marks <= 100:

        return jsonify({
            "error": "Marks must be between 0 and 100"
        }), 400

    conn = get_db_connection()

    cursor = conn.execute(
        """
        INSERT INTO students (name, marks)
        VALUES (?, ?)
        """,
        (name, marks)
    )

    student_id = cursor.lastrowid

    conn.commit()
    conn.close()

    return jsonify({
        "message": "Student added successfully",
        "student": {
            "id": student_id,
            "name": name,
            "marks": marks
        }
    }), 201


# ==========================================
# UPDATE STUDENT
# ==========================================

@app.route("/api/students/<int:student_id>", methods=["PUT"])
def update_student(student_id):

    auth_error = api_auth_required()

    if auth_error:

        return auth_error

    data = request.get_json(silent=True)

    if not data:

        return jsonify({
            "error": "JSON body is required"
        }), 400

    name = str(data.get("name", "")).strip()
    marks = data.get("marks")

    if not name:

        return jsonify({
            "error": "Name is required"
        }), 400

    if marks is None:

        return jsonify({
            "error": "Marks are required"
        }), 400

    try:

        marks = int(marks)

    except (ValueError, TypeError):

        return jsonify({
            "error": "Marks must be a number"
        }), 400

    if not 0 <= marks <= 100:

        return jsonify({
            "error": "Marks must be between 0 and 100"
        }), 400

    conn = get_db_connection()

    existing = conn.execute(
        """
        SELECT id
        FROM students
        WHERE id = ?
        """,
        (student_id,)
    ).fetchone()

    if existing is None:

        conn.close()

        return jsonify({
            "error": "Student not found"
        }), 404

    conn.execute(
        """
        UPDATE students
        SET name = ?, marks = ?
        WHERE id = ?
        """,
        (name, marks, student_id)
    )

    conn.commit()
    conn.close()

    return jsonify({
        "message": "Student updated successfully",
        "student": {
            "id": student_id,
            "name": name,
            "marks": marks
        }
    }), 200


# ==========================================
# DELETE STUDENT
# ==========================================

@app.route("/api/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):

    auth_error = api_auth_required()

    if auth_error:

        return auth_error

    conn = get_db_connection()

    existing = conn.execute(
        """
        SELECT id
        FROM students
        WHERE id = ?
        """,
        (student_id,)
    ).fetchone()

    if existing is None:

        conn.close()

        return jsonify({
            "error": "Student not found"
        }), 404

    conn.execute(
        """
        DELETE FROM students
        WHERE id = ?
        """,
        (student_id,)
    )

    conn.commit()
    conn.close()

    return jsonify({
        "message": "Student deleted successfully"
    }), 200


# ==========================================
# SEARCH STUDENTS
# ==========================================

@app.route("/api/students/search", methods=["GET"])
def search_students():

    auth_error = api_auth_required()

    if auth_error:

        return auth_error

    name = request.args.get("name", "").strip()

    if not name:

        return jsonify({
            "error": "Name query parameter is required"
        }), 400

    conn = get_db_connection()

    students = conn.execute(
        """
        SELECT id, name, marks
        FROM students
        WHERE name LIKE ?
        ORDER BY id
        """,
        (f"%{name}%",)
    ).fetchall()

    conn.close()

    result = []

    for student in students:

        result.append({
            "id": student["id"],
            "name": student["name"],
            "marks": student["marks"]
        })

    return jsonify(result), 200


# ==========================================
# RUN APPLICATION
# ==========================================

if __name__ == "__main__":

    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    )