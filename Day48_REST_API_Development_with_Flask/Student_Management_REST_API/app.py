from flask import Flask, jsonify, request  # type: ignore

app = Flask(__name__)


# Sample student data
students = [
    {
        "id": 1,
        "name": "Rahul",
        "marks": 85
    },
    {
        "id": 2,
        "name": "Priya",
        "marks": 95
    }
]


# --------------------------------------------------
# GET ALL STUDENTS
# --------------------------------------------------

@app.route("/students", methods=["GET"])
def get_students():
    return jsonify(students), 200


# --------------------------------------------------
# GET ONE STUDENT
# --------------------------------------------------

@app.route("/students/<int:student_id>", methods=["GET"])
def get_student(student_id):

    for student in students:

        if student["id"] == student_id:
            return jsonify(student), 200

    return jsonify({
        "error": "Student not found"
    }), 404


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

    if not 0 <= marks <= 100:
        return jsonify({
            "error": "Marks must be between 0 and 100"
        }), 400

    # Generate new ID
    new_id = max([student["id"] for student in students], default=0) + 1

    student = {
        "id": new_id,
        "name": data["name"],
        "marks": marks
    }

    students.append(student)

    return jsonify({
        "message": "Student added",
        "student": student
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

    if not 0 <= marks <= 100:
        return jsonify({
            "error": "Marks must be between 0 and 100"
        }), 400

    for student in students:

        if student["id"] == student_id:

            student["name"] = data["name"]
            student["marks"] = marks

            return jsonify({
                "message": "Student updated",
                "student": student
            }), 200

    return jsonify({
        "error": "Student not found"
    }), 404


# --------------------------------------------------
# DELETE STUDENT
# --------------------------------------------------

@app.route("/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):

    for student in students:

        if student["id"] == student_id:

            students.remove(student)

            return jsonify({
                "message": "Student deleted"
            }), 200

    return jsonify({
        "error": "Student not found"
    }), 404


# --------------------------------------------------
# RUN FLASK
# --------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)