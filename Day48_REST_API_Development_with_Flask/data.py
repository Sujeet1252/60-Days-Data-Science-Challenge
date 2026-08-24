from flask import Flask, jsonify, request

app = Flask(__name__)


students = [
    {
        "id": 1,
        "name": "Rahul",
        "marks": 85
    },
    {
        "id": 2,
        "name": "Priya",
        "marks": 92
    }
]


# GET ALL
@app.route("/students", methods=["GET"])
def get_students():

    return jsonify(students)


# GET ONE
@app.route("/students/<int:student_id>", methods=["GET"])
def get_student(student_id):

    for student in students:

        if student["id"] == student_id:

            return jsonify(student)

    return jsonify({
        "error": "Student not found"
    }), 404


# CREATE
@app.route("/students", methods=["POST"])
def add_student():

    data = request.get_json()

    students.append(data)

    return jsonify({
        "message": "Student added",
        "student": data
    }), 201


# UPDATE
@app.route(
    "/students/<int:student_id>",
    methods=["PUT"]
)
def update_student(student_id):

    data = request.get_json()

    for student in students:

        if student["id"] == student_id:

            student.update(data)

            return jsonify({
                "message": "Student updated",
                "student": student
            })

    return jsonify({
        "error": "Student not found"
    }), 404


# DELETE
@app.route(
    "/students/<int:student_id>",
    methods=["DELETE"]
)
def delete_student(student_id):

    for student in students:

        if student["id"] == student_id:

            students.remove(student)

            return jsonify({
                "message": "Student deleted"
            })

    return jsonify({
        "error": "Student not found"
    }), 404


if __name__ == "__main__":
    app.run(debug=True)