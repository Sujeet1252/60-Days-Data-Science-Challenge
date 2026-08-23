#!/usr/bin/env python
# coding: utf-8

# In[5]:


import sqlite3

conn = sqlite3.connect("student.db")

cursor = conn.cursor()

cursor.execute("""
Insert into Student 
Values(1,'Sujeet',90)
""")

conn.commit()

print("Data Inserted")

