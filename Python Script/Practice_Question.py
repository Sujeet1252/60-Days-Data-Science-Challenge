#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3

conn = sqlite3.connect("Practice.db")

cursor = conn.cursor()


# In[2]:


cursor.execute("""
CREATE TABLE Employee(
    id INTEGER PRIMARY KEY,
    name TEXT,
    salary INTEGER
);
""")


# In[3]:


cursor.execute("""
INSERT INTO Employee VALUES
(1,'Aman',50000),
(2,'Rahul',70000),
(3,'Priya',80000),
(4,'Neha',60000),
(5,'Rohit',55000);
""")
conn.commit()


# In[7]:


cursor.execute("""
SELECT * FROM Employee
""")
for rows in cursor.fetchall():
    print(rows)


# In[9]:


#Show employees sorted by salary

cursor.execute("""
SELECT * FROM Employee
ORDER BY Salary;
""")
for rows in cursor.fetchall():
    print(rows)


# In[10]:


#Show highest-paid employee

cursor.execute("""
SELECT * FROM Employee
ORDER BY Salary DESC
LIMIT 1;
""")
for rows in cursor.fetchall():
    print(rows)


# In[11]:


#Show Lowest-paid employee

cursor.execute("""
SELECT * FROM Employee
ORDER BY Salary ASC
LIMIT 1;
""")
for rows in cursor.fetchall():
    print(rows)


# In[13]:


#Display top 3 salaries

cursor.execute("""
SELECT * FROM Employee
ORDER BY Salary DESC
LIMIT 3;
""")
for rows in cursor.fetchall():
    print(rows)


# In[14]:


#Show employee having second-highest salary.

cursor.execute("""
SELECT * FROM Employee
ORDER BY Salary DESC
LIMIT 1 OFFSET 1;
""")
for rows in cursor.fetchall():
    print(rows)


# In[16]:


#Sort employees alphabetically by name

cursor.execute("""
SELECT * FROM Employee
ORDER BY Name ;
""")
for rows in cursor.fetchall():
    print(rows)


# In[ ]:




