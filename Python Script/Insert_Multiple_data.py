#!/usr/bin/env python
# coding: utf-8

# In[13]:


import sqlite3

conn = sqlite3.connect("student.db")

cursor = conn.cursor()

student= [
    (2,"Rahul",85),
    (3,"Mohit",80),
    (4,"Ram",90),
    (5,"Sam",75)
]

cursor.executemany(
"Insert  Or Ignore Into Student Values (?,?,?)", student
)
conn.commit()

print("Student Added")

