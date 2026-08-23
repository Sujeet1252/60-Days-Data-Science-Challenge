#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3

conn = sqlite3.connect("Practice.db")

cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS Faculty")

cursor.execute("""
CREATE TABLE Faculty(
    id INTEGER,
    name TEXT,
    department TEXT,
    salary INTEGER,
    experience INTEGER
)
""")

# Insert Data
Faculty = [
    (1,'Aman','MCA',50000,2),
    (2,'Rahul','MBA',70000,5),
    (3,'Priya','MBA',45000,3),
    (4,'Neha','CSE',55000,4),
    (5,'Rohit','IT',65000,6),
    (6,'Karan','MCA',60000,4),
    (7,'Anjali','MBA',80000,7)
]

cursor.executemany(
    "INSERT INTO Faculty VALUES (?,?,?,?,?)",
    Faculty
)

conn.commit()

print("Database Ready!")


# In[2]:


cursor.execute("""
SELECT COUNT(*)
FROM Faculty;
""")
for rows in cursor.fetchall():
    print("Total Faculty :",rows)


# In[4]:


cursor.execute("""
SELECT SUM(Salary)
FROM Faculty;
""")
for rows in cursor.fetchall():
    print("Total Salary :",rows)


# In[5]:


cursor.execute("""
SELECT AVG(Salary)
FROM Faculty;
""")
for rows in cursor.fetchall():
    print("Average Salary :",rows)


# In[6]:


cursor.execute("""
SELECT MAX(Salary)
FROM Faculty;
""")
for rows in cursor.fetchall():
    print("Maximum Salary :",rows)


# In[8]:


cursor.execute("""
SELECT Department,
    COUNT()
    FROM faculty
    GROUP BY Department;
""")
for rows in cursor.fetchall():
    print("Faculty  :",rows)


# In[11]:


cursor.execute("""
SELECT Department,
    AVG(Salary)
    FROM faculty
    GROUP BY Department;
""")
for rows in cursor.fetchall():
    print(" Average Salary  :",rows)


# In[15]:


cursor.execute("""
SELECT Department,
    AVG(Salary) 
    FROM Faculty
    GROUP BY Department
    HAVING AVG(Salary) > 50000;
""")
for rows in cursor.fetchall():
    print(" Average Salary according to department  :",rows)

