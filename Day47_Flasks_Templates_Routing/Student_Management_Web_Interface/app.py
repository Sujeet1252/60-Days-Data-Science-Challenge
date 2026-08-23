from flask import Flask, render_template, abort

app = Flask(__name__)

students = [
    {
        "id": 1,
        "name": "John Doe",
        "marks": 85
    },
    {
        "id": 2, 
        "name": "Jane Smith",
        "marks": 92 
    },
    {
        "id": 3,
        "name": "Alice Johnson",
        "marks": 78
    }
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route("/students")
def student_list():
    return render_template("students.html", students=students)

@app.route('/students/<int:student_id>')
def student_detail(student_id):
    student = next(
        (student for student in students if student["id"] == student_id),
         None
    )
    if not student:
        abort(404)
    return render_template('student.html', student=student)

if __name__ == '__main__':
    app.run(debug=True)