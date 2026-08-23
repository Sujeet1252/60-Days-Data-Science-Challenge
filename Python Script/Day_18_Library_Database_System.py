#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3

conn = sqlite3.connect("Library.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Students(
    StudentID INTEGER PRIMARY KEY,
    Name TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Books(
    BookID INTEGER PRIMARY KEY,
    BookName TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Borrow(
    StudentID INTEGER,
    BookID INTEGER
)
""")

cursor.execute("DELETE FROM Students")
cursor.execute("DELETE FROM Books")
cursor.execute("DELETE FROM Borrow")

students = [
    (1, "Rahul"),
    (2, "Priya"),
    (3, "Aman"),
    (4, "Neha"),
    (5, "Rohit")
]

books = [
    (101, "Python Basics"),
    (102, "SQL Mastery"),
    (103, "Data Science"),
    (104, "Machine Learning"),
    (105, "Statistics")
]

borrow = [
    (1, 101),
    (2, 103),
    (3, 102),
    (4, 105),
    (5, 104)
]

cursor.executemany(
    "INSERT INTO Students VALUES(?,?)",
    students
)

cursor.executemany(
    "INSERT INTO Books VALUES(?,?)",
    books
)

cursor.executemany(
    "INSERT INTO Borrow VALUES(?,?)",
    borrow
)

conn.commit()

print("\nSTUDENT + BOOK DETAILS\n")

cursor.execute("""
SELECT Students.Name,
       Books.BookName
FROM Borrow
INNER JOIN Students
ON Borrow.StudentID = Students.StudentID
INNER JOIN Books
ON Borrow.BookID = Books.BookID
""")

for row in cursor.fetchall():
    print(row)

conn.close()


# In[ ]:




