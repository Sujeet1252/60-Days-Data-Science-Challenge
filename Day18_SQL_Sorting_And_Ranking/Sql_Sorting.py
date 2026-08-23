#!/usr/bin/env python
# coding: utf-8

# In[2]:


import sqlite3

conn = sqlite3.connect("Employee.db")

cursor = conn.cursor()


# In[3]:


cursor.execute("""
CREATE TABLE Employee(
    id INTEGER PRIMARY KEY,
    name TEXT,
    salary INTEGER
);
""")



# In[5]:


cursor.execute("""
INSERT INTO Employee VALUES
(1,'Aman',50000),
(2,'Rahul',70000),
(3,'Priya',80000),
(4,'Neha',60000),
(5,'Rohit',55000);
""")
conn.commit()


# In[6]:


cursor.execute("""
SELECT * FROM Employee
""")

rows = cursor.fetchall()

for row in rows:
    print(row)


# In[7]:


#ORder By

cursor.execute("""
SELECT *
FROM Employee
ORDER BY Salary;
""")

rows = cursor.fetchall()

for row in rows:
    print(row)


# In[8]:


#Ascending order 

cursor.execute("""
SELECT *
FROM Employee
ORDER BY Salary ASC;
""")

rows = cursor.fetchall()

for row in rows:
    print(row)


# In[9]:


#descending order 

cursor.execute("""
SELECT *
FROM Employee
ORDER BY Salary DESC;
""")

rows = cursor.fetchall()

for row in rows:
    print(row)


# In[10]:


#Limit used to restrict rows return

cursor.execute("""
SELECT *
FROM Employee
LIMIT 3;
""")

rows = cursor.fetchall()

for row in rows:
    print(row)


# In[11]:


#Highest Salary

cursor.execute("""
SELECT *
FROM Employee
ORDER BY Salary DESC
LIMIT 1;
""")

rows = cursor.fetchall()

for row in rows:
    print(row)


# In[12]:


#HLowest Salary

cursor.execute("""
SELECT *
FROM Employee
ORDER BY Salary ASC
LIMIT 1;
""")

rows = cursor.fetchall()

for row in rows:
    print(row)


# In[ ]:




