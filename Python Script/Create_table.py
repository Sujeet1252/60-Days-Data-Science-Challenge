#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3 

conn = sqlite3.connect("student.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Student(
    ID INTEGER PRIMARY KEY,
    Name TEXT,
    Marks INTEGER
)
""")

print("Table created successfully")

