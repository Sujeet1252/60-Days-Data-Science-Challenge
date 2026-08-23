#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3
import pandas as pd

# Create Database
conn = sqlite3.connect("company.db")

cursor = conn.cursor()

# Drop table if exists
cursor.execute("DROP TABLE IF EXISTS Employee")

# Create Table
cursor.execute("""
CREATE TABLE Employee(
    id INTEGER,
    name TEXT,
    department TEXT,
    salary INTEGER,
    experience INTEGER
)
""")

# Insert Data
employee = [
    (1,'Aman','IT',50000,2),
    (2,'Rahul','IT',70000,5),
    (3,'Priya','HR',45000,3),
    (4,'Neha','HR',55000,4),
    (5,'Rohit','Sales',65000,6),
    (6,'Karan','Sales',60000,4),
    (7,'Anjali','IT',80000,7)
]

cursor.executemany(
    "INSERT INTO Employee VALUES (?,?,?,?,?)",
    employees
)

conn.commit()

print("Database Ready!")


# In[3]:


#COUNT TOATL ROWS

cursor.execute("""
SELECT COUNT(*)
FROM Employee;
""") 

for rows in cursor.fetchall():
    print(rows)


# In[4]:


#CALCULATE TOTAL SALARY

cursor.execute("""
SELECT SUM(Salary)
FROM Employee;
""") 

for rows in cursor.fetchall():
    print(rows)


# In[5]:


#CALCULATE AVERAGE SALARY

cursor.execute("""
SELECT AVG(Salary)
FROM Employee;
""") 

for rows in cursor.fetchall():
    print(rows)


# In[6]:


#CLCULATE MAXIMUM SALARY

cursor.execute("""
SELECT MAX(Salary)
FROM Employee;
""") 

for rows in cursor.fetchall():
    print(rows)


# In[7]:


#CALCULATE MINIMUM SALARY

cursor.execute("""
SELECT MIN(Salary)
FROM Employee;
""") 

for rows in cursor.fetchall():
    print(rows)


# In[8]:


#GROUP BY

cursor.execute("""
SELECT Department,
       AVG(Salary)
FROM Employee
GROUP BY Department;
""") 

for rows in cursor.fetchall():
    print(rows)


# In[9]:


#HAVING 

cursor.execute("""
SELECT Department,
       AVG(Salary)
FROM Employee
GROUP BY Department
HAVING AVG(Salary) > 50000;
""") 

for rows in cursor.fetchall():
    print(rows)

