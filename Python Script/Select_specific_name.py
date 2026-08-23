#!/usr/bin/env python
# coding: utf-8

# In[2]:


import sqlite3

conn = sqlite3.connect("student.db")

cursor = conn.cursor()

cursor.execute("""
SELECT Name FROM Student
""")

print(cursor.fetchall())

