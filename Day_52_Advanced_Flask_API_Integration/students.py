from flask import Blueprint  # type: ignore

students_bp = Blueprint('students', __name__)

@students_bp.route('/students')
def get_students():
    
    return "List of students"