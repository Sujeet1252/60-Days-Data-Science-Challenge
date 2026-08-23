#!/usr/bin/env python
# coding: utf-8

# In[3]:


import sqlite3 

conn = sqlite3.connect("Project2.db")

cursor = conn.cursor()


# In[4]:


cursor.execute("""
CREATE TABLE Employee(
    id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    salary INTEGER,
    experience INTEGER
);
""")

conn.commit()


# In[5]:


cursor.execute("""
INSERT INTO Employee VALUES
(1,"Sujeet","IT",50000,2),
(2,"Rohit","HR",47000,3),
(3,"Mayank","IT",45000,2),
(4,"Saurabh","Finance",40000,1),
(5,"Sunil","HR",42000,3),
(6,"Arpit","Marketing",45000,3),
(7,"Pratham","HR",55000,3)
""")
conn.commit()



# In[6]:


cursor.execute("SELECT * from Employee")

for rows in cursor.fetchall():
    print(rows)


# In[8]:


# HIGHEST SALARY

cursor.execute("""
SELECT * FROM Employee
ORDER BY Salary DESC
LIMIT 1;
""")
for rows in cursor.fetchall():
    print(rows)


# In[9]:


# TOP 3 SALARY

cursor.execute("""
SELECT * FROM Employee
ORDER BY Salary DESC
LIMIT 3;
""")
for rows in cursor.fetchall():
    print(rows)


# In[10]:


# LOWEST SALARY

cursor.execute("""
SELECT * FROM Employee
ORDER BY Salary ASC
LIMIT 1;
""")
for rows in cursor.fetchall():
    print(rows)


# In[17]:


#MOST EXPERIENCED EMPLOYEE

cursor.execute("""
SELECT *
FROM Employee
WHERE Salary > 50000
ORDER BY Experience DESC
LIMIT 1;
""")
for rows in cursor.fetchall():
    print(rows)


# In[18]:


# TOP 3 EXPERIENCED EMPLOYEES

cursor.execute("""
SELECT *
FROM Employee
ORDER BY Experience DESC
LIMIT 3;
""")
for rows in cursor.fetchall():
    print(rows)


# In[ ]:




