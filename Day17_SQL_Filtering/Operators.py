#!/usr/bin/env python
# coding: utf-8

# In[6]:


import sqlite3

conn = sqlite3.connect("Practice.db")

cursor = conn.cursor()

cursor.execute ("""
CREATE TABLE IF NOT EXISTS Practice(
    INT ID PRIMARY KEY,
    Name TEXT,
    Department TEXT,
    Salary INTEGER
)
""")


# In[8]:


cursor.execute("DELETE FROM Practice")

cursor.execute("""
INSERT INTO Practice
VALUES(1,'Aman','IT',50000)
""")

cursor.execute("""
INSERT INTO Practice
VALUES(2,'Rahul','HR',45000)
""")

cursor.execute("""
INSERT INTO Practice
VALUES(3,'Priya','Finance',70000)
""")

cursor.execute("""
INSERT INTO Practice
VALUES(4,'Neha','IT',60000)
""")

cursor.execute("""
INSERT INTO Practice
VALUES(5,'Rohit','Marketing',55000)
""")

conn.commit()


# In[9]:


cursor.execute(" Select * FROM Practice ")

rows = cursor.fetchall()

for row in rows:
    print(row)



# In[12]:


#Greater than operator

cursor.execute("""
SELECT * FROM Practice
WHERE Salary > 55000

""")

for row in cursor.fetchall():
    print(row)


# In[13]:


#Equal to Operator

cursor.execute("""
SELECT * FROM Practice
WHERE Name = 'Neha'

""")

for row in cursor.fetchall():
    print(row)


# In[14]:


#Not Equal to operator

cursor.execute("""
SELECT * FROM Practice
WHERE Salary != 55000

""")

for row in cursor.fetchall():
    print(row)


# In[15]:


# And Operator

cursor.execute("""
SELECT * FROM Practice
WHERE Salary > 55000
AND Department = 'IT'
""")

for row in cursor.fetchall():
    print(row)


# In[16]:


# OR operator

cursor.execute("""
SELECT * FROM Practice
WHERE Department = 'IT'
OR Department = 'HR'
""")

for row in cursor.fetchall():
    print(row)


# In[18]:


# Not operator

cursor.execute("""
SELECT * FROM Practice
WHERE NOT Department 'HR'

""")

for row in cursor.fetchall():
    print(row)

