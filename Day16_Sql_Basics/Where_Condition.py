#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3

conn = sqlite3.connect("student.db")

cursor = conn.cursor()

cursor.execute("""
SELECT *
FROM Student
WHERE Marks > 85
""")

print(cursor.fetchall())

