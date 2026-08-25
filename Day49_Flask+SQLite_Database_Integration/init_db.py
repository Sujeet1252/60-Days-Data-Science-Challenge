import sqlite3

connection = sqlite3.connect("students.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    marks INTEGER NOT NULL
)
""")
cursor.execute("""
INSERT INTO students (name, marks)
VALUES (?, ?)
""", ("Rahul", 85))

connection.commit()

connection.close()

print("Database created successfully!")