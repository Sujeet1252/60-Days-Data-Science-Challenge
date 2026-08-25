from flask import Flask, jsonify, request  # type: ignore
import sqlite3

app = Flask(__name__)

def get_db_connection():

    connection = sqlite3.connect("students.db")
    connection.row_factory = sqlite3.Row
    return connection


@app.route(
    "/students",
    methods=["GET"]
)
def get_students():

    connection = get_db_connection()

    students = connection.execute(
        "SELECT * FROM students"
    ).fetchall()

    connection.close()

    return jsonify([
        dict(student)
        for student in students
    ])

@app.route(
    "/students/<int:student_id>",
    methods=["GET"]
)
def get_student(student_id):

    connection = get_db_connection()

    student = connection.execute(
        "SELECT * FROM students WHERE id = ?",
        (student_id,)
    ).fetchone()

    connection.close()

    if student is None:

        return jsonify({
            "error": "Student not found"
        }), 404

    return jsonify(dict(student))

@app.route(
    "/students",
    methods=["POST"]
)
def add_student():

    data = request.get_json()

    name = data.get("name")
    marks = data.get("marks")

    if not name or marks is None:

        return jsonify({
            "error": "Name and marks are required"
        }), 400

    if not 0 <= marks <= 100:

        return jsonify({
            "error": "Marks must be between 0 and 100"
        }), 400

    connection = get_db_connection()

    cursor = connection.execute(
        """
        INSERT INTO students (name, marks)
        VALUES (?, ?)
        """,
        (name, marks)
    )

    connection.commit()

    student_id = cursor.lastrowid

    connection.close()

    return jsonify({
        "message": "Student added successfully",
        "id": student_id
    }), 201

@app.route(
    "/students/<int:student_id>",
    methods=["PUT"]
)
def update_student(student_id):

    data = request.get_json()

    name = data.get("name")
    marks = data.get("marks")

    if not name or marks is None:

        return jsonify({
            "error": "Name and marks are required"
        }), 400

    if not 0 <= marks <= 100:

        return jsonify({
            "error": "Marks must be between 0 and 100"
        }), 400

    connection = get_db_connection()

    cursor = connection.execute(
        """
        UPDATE students
        SET name = ?, marks = ?
        WHERE id = ?
        """,
        (name, marks, student_id)
    )

    connection.commit()

    if cursor.rowcount == 0:

        connection.close()

        return jsonify({
            "error": "Student not found"
        }), 404

    connection.close()

    return jsonify({
        "message": "Student updated successfully"
    })

@app.route(
    "/students/<int:student_id>",
    methods=["DELETE"]
)
def delete_student(student_id):

    connection = get_db_connection()

    cursor = connection.execute(
        "DELETE FROM students WHERE id = ?",
        (student_id,)
    )

    connection.commit()

    if cursor.rowcount == 0:

        connection.close()

        return jsonify({
            "error": "Student not found"
        }), 404

    connection.close()

    return jsonify({
        "message": "Student deleted successfully"
    })

if __name__ == "__main__":
    app.run(debug=True)