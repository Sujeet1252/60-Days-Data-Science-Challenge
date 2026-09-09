from flask import Blueprint, request, session  # type: ignore

from database.db import get_db_connection
from utils.responses import success_response, error_response


# ============================================================
# STUDENTS BLUEPRINT
# ============================================================

students_bp = Blueprint(
    "students",
    __name__,
    url_prefix="/api"
)


# ============================================================
# AUTHENTICATION CHECK
# ============================================================

def authenticated():
    return "user_id" in session


# ============================================================
# GET ALL STUDENTS
# GET /api/students
# ============================================================

@students_bp.route("/students", methods=["GET"])
def get_students():

    if not authenticated():
        return error_response("Authentication required", 401)

    connection = get_db_connection()

    students = connection.execute(
        """
        SELECT id, name, marks
        FROM students
        WHERE user_id = ?
        """,
        (session["user_id"],)
    ).fetchall()

    connection.close()

    return success_response(
        "Students fetched successfully",
        [dict(student) for student in students]
    )


# ============================================================
# GET SINGLE STUDENT
# GET /api/students/<student_id>
# ============================================================

@students_bp.route("/students/<int:student_id>", methods=["GET"])
def get_student(student_id):

    if not authenticated():
        return error_response("Authentication required", 401)

    connection = get_db_connection()

    student = connection.execute(
        """
        SELECT id, name, marks
        FROM students
        WHERE id = ? AND user_id = ?
        """,
        (student_id, session["user_id"])
    ).fetchone()

    connection.close()

    if student is None:
        return error_response("Student not found", 404)

    return success_response(
        "Student fetched successfully",
        dict(student)
    )


# ============================================================
# ADD STUDENT
# POST /api/students
# ============================================================

@students_bp.route("/students", methods=["POST"])
def add_student():

    if not authenticated():
        return error_response("Authentication required", 401)

    data = request.get_json(silent=True)

    if not data:
        return error_response("JSON body is required", 400)

    name = data.get("name")
    marks = data.get("marks")

    # -------------------------
    # Validate name
    # -------------------------

    if not name:
        return error_response("Name is required", 400)

    # -------------------------
    # Validate marks
    # -------------------------

    if marks is None:
        return error_response("Marks are required", 400)

    if not isinstance(marks, int):
        return error_response("Marks must be an Integer", 400)

    if marks < 0 or marks > 100:
        return error_response(
            "Marks must be between 0 and 100",
            400
        )

    # -------------------------
    # Insert student
    # -------------------------

    connection = get_db_connection()

    cursor = connection.execute(
        """
        INSERT INTO students (name, marks, user_id)
        VALUES (?, ?, ?)
        """,
        (name, marks, session["user_id"])
    )

    connection.commit()

    student_id = cursor.lastrowid

    connection.close()

    return success_response(
        "Student added successfully",
        {
            "id": student_id,
            "name": name,
            "marks": marks
        }
    )


# ============================================================
# UPDATE STUDENT
# PUT /api/students/<student_id>
# ============================================================

@students_bp.route("/students/<int:student_id>", methods=["PUT"])
def update_student(student_id):

    if not authenticated():
        return error_response("Authentication required", 401)

    data = request.get_json(silent=True)

    if not data:
        return error_response("JSON body is required", 400)

    name = data.get("name")
    marks = data.get("marks")

    # -------------------------
    # Validate name
    # -------------------------

    if not name:
        return error_response("Name is required", 400)

    # -------------------------
    # Validate marks
    # -------------------------

    if marks is None:
        return error_response("Marks are required", 400)

    if not isinstance(marks, int):
        return error_response("Marks must be an Integer", 400)

    if marks < 0 or marks > 100:
        return error_response(
            "Marks must be between 0 and 100",
            400
        )

    connection = get_db_connection()

    # -------------------------
    # Check student exists
    # -------------------------

    student = connection.execute(
        """
        SELECT id
        FROM students
        WHERE id = ? AND user_id = ?
        """,
        (student_id, session["user_id"])
    ).fetchone()

    if student is None:
        connection.close()
        return error_response("Student not found", 404)

    # -------------------------
    # Update student
    # -------------------------

    connection.execute(
        """
        UPDATE students
        SET name = ?, marks = ?
        WHERE id = ? AND user_id = ?
        """,
        (
            name,
            marks,
            student_id,
            session["user_id"]
        )
    )

    connection.commit()

    connection.close()

    return success_response(
        "Student updated successfully",
        {
            "id": student_id,
            "name": name,
            "marks": marks
        }
    )


# ============================================================
# DELETE STUDENT
# DELETE /api/students/<student_id>
# ============================================================

@students_bp.route("/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):

    if not authenticated():
        return error_response("Authentication required", 401)

    connection = get_db_connection()

    # -------------------------
    # Check student exists
    # -------------------------

    student = connection.execute(
        """
        SELECT id, name, marks
        FROM students
        WHERE id = ? AND user_id = ?
        """,
        (student_id, session["user_id"])
    ).fetchone()

    if student is None:
        connection.close()
        return error_response("Student not found", 404)

    # -------------------------
    # Delete student
    # -------------------------

    connection.execute(
        """
        DELETE FROM students
        WHERE id = ? AND user_id = ?
        """,
        (student_id, session["user_id"])
    )

    connection.commit()

    connection.close()

    return success_response(
        "Student deleted successfully",
        dict(student)
    )