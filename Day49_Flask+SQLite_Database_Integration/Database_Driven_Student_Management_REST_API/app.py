# pyright: reportMissingImports=false
from flask import Flask, jsonify, request  # noqa: E402
import sqlite3

app = Flask(__name__)

DATABASE = "students.db"


# --------------------------------------------------
# DATABASE CONNECTION
# --------------------------------------------------

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


# --------------------------------------------------
# CREATE DATABASE AND TABLE
# --------------------------------------------------

def init_db():

    conn = get_db_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            marks INTEGER NOT NULL
        )
    """)

    conn.commit()
    conn.close()


# --------------------------------------------------
# GET ALL STUDENTS
# --------------------------------------------------

@app.route("/students", methods=["GET"])
def get_students():

    conn = get_db_connection()

    students = conn.execute(
        "SELECT * FROM students"
    ).fetchall()

    conn.close()

    return jsonify([dict(student) for student in students]), 200


# --------------------------------------------------
# GET ONE STUDENT
# --------------------------------------------------

@app.route("/students/<int:student_id>", methods=["GET"])
def get_student(student_id):

    conn = get_db_connection()

    student = conn.execute(
        "SELECT * FROM students WHERE id = ?",
        (student_id,)
    ).fetchone()

    conn.close()

    if student is None:
        return jsonify({
            "error": "Student not found"
        }), 404

    return jsonify(dict(student)), 200


# --------------------------------------------------
# ADD STUDENT
# --------------------------------------------------

@app.route("/students", methods=["POST"])
def add_student():

    data = request.get_json()

    if not data:
        return jsonify({
            "error": "JSON body is required"
        }), 400

    # Validate name
    if not data.get("name"):
        return jsonify({
            "error": "Name is required"
        }), 400

    # Validate marks
    marks = data.get("marks")

    if marks is None:
        return jsonify({
            "error": "Marks are required"
        }), 400

    if not isinstance(marks, int):
        return jsonify({
            "error": "Marks must be an integer"
        }), 400

    if not 0 <= marks <= 100:
        return jsonify({
            "error": "Marks must be between 0 and 100"
        }), 400

    conn = get_db_connection()

    cursor = conn.execute(
        "INSERT INTO students (name, marks) VALUES (?, ?)",
        (data["name"], marks)
    )

    conn.commit()

    new_id = cursor.lastrowid

    conn.close()

    return jsonify({
        "message": "Student added",
        "student": {
            "id": new_id,
            "name": data["name"],
            "marks": marks
        }
    }), 201


# --------------------------------------------------
# UPDATE STUDENT
# --------------------------------------------------

@app.route("/students/<int:student_id>", methods=["PUT"])
def update_student(student_id):

    data = request.get_json()

    if not data:
        return jsonify({
            "error": "JSON body is required"
        }), 400

    # Validate name
    if not data.get("name"):
        return jsonify({
            "error": "Name is required"
        }), 400

    # Validate marks
    marks = data.get("marks")

    if marks is None:
        return jsonify({
            "error": "Marks are required"
        }), 400

    if not isinstance(marks, int):
        return jsonify({
            "error": "Marks must be an integer"
        }), 400

    if not 0 <= marks <= 100:
        return jsonify({
            "error": "Marks must be between 0 and 100"
        }), 400

    conn = get_db_connection()

    student = conn.execute(
        "SELECT * FROM students WHERE id = ?",
        (student_id,)
    ).fetchone()

    if student is None:

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
        (data["name"], marks, student_id)
    )

    conn.commit()
    conn.close()

    return jsonify({
        "message": "Student updated",
        "student": {
            "id": student_id,
            "name": data["name"],
            "marks": marks
        }
    }), 200


# --------------------------------------------------
# DELETE STUDENT
# --------------------------------------------------

@app.route("/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):

    conn = get_db_connection()

    student = conn.execute(
        "SELECT * FROM students WHERE id = ?",
        (student_id,)
    ).fetchone()

    if student is None:

        conn.close()

        return jsonify({
            "error": "Student not found"
        }), 404

    conn.execute(
        "DELETE FROM students WHERE id = ?",
        (student_id,)
    )

    conn.commit()
    conn.close()

    return jsonify({
        "message": "Student deleted"
    }), 200


# --------------------------------------------------
# BONUS - SEARCH STUDENTS
# --------------------------------------------------

@app.route("/students/search", methods=["GET"])
def search_students():

    name = request.args.get("name")

    if not name:
        return jsonify({
            "error": "Name query parameter is required"
        }), 400

    conn = get_db_connection()

    students = conn.execute(
        """
        SELECT * FROM students
        WHERE name LIKE ?
        """,
        (f"%{name}%",)
    ).fetchall()

    conn.close()

    return jsonify([
        dict(student)
        for student in students
    ]), 200


# --------------------------------------------------
# RUN APPLICATION
# --------------------------------------------------

if __name__ == "__main__":

    init_db()

    app.run(debug=True)