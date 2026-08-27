import sqlite3
from werkzeug.security import generate_password_hash

DATABASE = "database.db"


def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # -------------------------
    # USERS TABLE
    # -------------------------
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)

    # -------------------------
    # STUDENTS TABLE
    # -------------------------
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            marks INTEGER NOT NULL
        )
    """)

    conn.commit()

    # Create a default user if users table is empty
    cursor.execute("SELECT COUNT(*) FROM users")
    user_count = cursor.fetchone()[0]

    if user_count == 0:

        password_hash = generate_password_hash("test123")

        cursor.execute(
            """
            INSERT INTO users (username, password)
            VALUES (?, ?)
            """,
            ("test", password_hash)
        )

    # Add some sample students if table is empty
    cursor.execute("SELECT COUNT(*) FROM students")
    student_count = cursor.fetchone()[0]

    if student_count == 0:

        students = [
            ("Rahul", 85),
            ("Priya", 92),
            ("Aman", 88)
        ]

        cursor.executemany(
            """
            INSERT INTO students (name, marks)
            VALUES (?, ?)
            """,
            students
        )

    conn.commit()
    conn.close()

    print("Database initialized successfully.")
    print("Default login:")
    print("Username: test")
    print("Password: test123")


if __name__ == "__main__":
    init_db()