#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3

conn = sqlite3.connect("Project.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Project(
    INT ID PRIMARY KEY,
    NAME TEXT,
    DEPARTMENT TEXT,
    SALARY INT,
    CITY TEXT
)
""")


# In[2]:


cursor.execute("DELETE FROM Project")

Project = [
    (1,"Sujeet","IT",70000,"Varanasi"),
    (2,"Mayank","IT",50000,"Prayagraj"),
    (3,"Raju","Finance",45000,"Bhadoi"),
    (4,"Pratham","HR",75000,"Dehradun"),
    (5,"Saurabh","Finance",70000,"Dehradun")
]

cursor.executemany(
    "INSERT OR IGNORE INTO Project VALUES (?,?,?,?,?) ", Project
)

conn.commit()


# In[3]:


cursor.execute("""
SELECT *
FROM Project
WHERE Department='IT';
""")
for row in cursor.fetchall():
    print(row)


# In[3]:


cursor.execute("""
SELECT *
FROM Project
WHERE Department='IT';
""")
for row in cursor.fetchall():
    print(row)


# In[5]:


cursor.execute("""
SELECT * FROM Project
WHERE Salary > 50000;
""")
for row in cursor.fetchall():
    print(row)


# In[6]:


cursor.execute("""
SELECT * FROM Project
WHERE Department='IT'
AND Salary > 50000;
""")
for row in cursor.fetchall():
    print(row)


# In[7]:


cursor.execute("""
SELECT * FROM Project
WHERE City ='Dehradun'
OR City = 'Varanasi';
""")
for row in cursor.fetchall():
    print(row)

