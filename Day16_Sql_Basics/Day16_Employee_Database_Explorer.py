#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3

# ==========================
# DATABASE CONNECTION
# ==========================

conn = sqlite3.connect("employee.db")

cursor = conn.cursor()

# ==========================
# CREATE TABLE
# ==========================

cursor.execute("""
CREATE TABLE IF NOT EXISTS Employee(

    ID INTEGER PRIMARY KEY,
    Name TEXT,
    Department TEXT,
    Salary INTEGER

)
""")

# ==========================
# INSERT DATA
# ==========================

cursor.execute("DELETE FROM Employee")

cursor.execute("""
INSERT INTO Employee
VALUES(1,'Aman','IT',50000)
""")

cursor.execute("""
INSERT INTO Employee
VALUES(2,'Rahul','HR',45000)
""")

cursor.execute("""
INSERT INTO Employee
VALUES(3,'Priya','Finance',70000)
""")

cursor.execute("""
INSERT INTO Employee
VALUES(4,'Neha','IT',60000)
""")

cursor.execute("""
INSERT INTO Employee
VALUES(5,'Rohit','Marketing',55000)
""")

conn.commit()

# ==========================
# DISPLAY ALL EMPLOYEES
# ==========================

print("=" * 50)
print("EMPLOYEE DATABASE")
print("=" * 50)

cursor.execute("SELECT * FROM Employee")

rows = cursor.fetchall()

for row in rows:
    print(row)

# ==========================
# DISPLAY ONLY NAMES
# ==========================

print("\nEmployee Names")

cursor.execute("""
SELECT Name
FROM Employee
""")

for row in cursor.fetchall():
    print(row[0])

# ==========================
# NAME AND SALARY
# ==========================

print("\nName and Salary")

cursor.execute("""
SELECT Name, Salary
FROM Employee
""")

for row in cursor.fetchall():
    print(row)

# ==========================
# SALARY GREATER THAN 50000
# ==========================

print("\nEmployees With Salary > 50000")

cursor.execute("""
SELECT *
FROM Employee
WHERE Salary > 50000
""")

for row in cursor.fetchall():
    print(row)

# ==========================
# IT DEPARTMENT EMPLOYEES
# ==========================

print("\nIT Department Employees")

cursor.execute("""
SELECT *
FROM Employee
WHERE Department = 'IT'
""")

for row in cursor.fetchall():
    print(row)

# ==========================
# SALARY REPORT
# ==========================

cursor.execute("""
SELECT Salary
FROM Employee
""")

salaries = cursor.fetchall()

salary_list = []

for salary in salaries:
    salary_list.append(salary[0])

print("\n" + "=" * 50)
print("EMPLOYEE REPORT")
print("=" * 50)

print("Total Employees :", len(salary_list))
print("Highest Salary  :", max(salary_list))
print("Lowest Salary   :", min(salary_list))
print("Average Salary  :", round(sum(salary_list) / len(salary_list), 2))

print("=" * 50)

# ==========================
# CLOSE DATABASE
# ==========================

conn.close()

