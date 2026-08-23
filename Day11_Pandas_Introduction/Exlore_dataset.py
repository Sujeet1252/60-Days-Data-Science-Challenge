#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd

df = pd.read_csv("students.csv")

print(df)

print("\n    First five rows are :")
print(df.head())

print("\n    Last five rows are :")
print(df.tail())

print("\nInfo about this :")
print(df.info())

print("\ndescribe : ")
print(df.describe())

