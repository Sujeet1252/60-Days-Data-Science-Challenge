#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3

conn = sqlite3.connect("EMPLOYEE.db")

cursor = conn.cursor()

cursor.execute ("""
CREATE TABLE IF NOT EXISTS Employee(
    INT ID PRIMARY KEY,
    Name TEXT,
    Department TEXT,
    Salary INTEGER
)
""")


# In[3]:


cursor.execute("DELETE FROM Employee")

Employee = [
    (1,"Aman","IT",50000),
    (2,"Rahul","HR",40000),
    (4,"Priya","IT",70000),
    (5,"Neha","Finance",80000)
]

cursor.executemany(
"Insert  Or Ignore Into Employee Values (?,?,?,?)", Employee
)
conn.commit()


# In[4]:


cursor.execute("""
SELECT * FROM Employee
""")

rows = cursor.fetchall()

for row in rows:
    print(row)


# In[5]:


cursor.execute("""
SELECT *
FROM Employee
WHERE Salary > 50000;
""")

rows = cursor.fetchall()

for row in rows:
    print(row)


# In[6]:


cursor.execute("""
SELECT *
FROM Employee
WHERE Salary < 60000;
""")

rows = cursor.fetchall()

for row in rows:
    print(row)


# In[8]:


cursor.execute("""
SELECT *
FROM Employee
WHERE Department = 'IT';
""")

rows = cursor.fetchall()

for row in rows:
    print(row)


# In[9]:


cursor.execute("""
SELECT *
FROM Employee
WHERE Salary > 50000
AND Department = 'IT';
""")

rows = cursor.fetchall()

for row in rows:
    print(row)


# In[11]:


cursor.execute("""
SELECT *
FROM Employee
WHERE Department = 'IT'
OR Department = 'HR';
""")

rows = cursor.fetchall()

for row in rows:
    print(row)


# In[ ]:




