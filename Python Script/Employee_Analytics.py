#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd

data = {
    "Name": ["Aman","Rahul","Priya","Neha","Rohit"],
    "Department": ["IT","HR","IT","Finance","HR"],
    "Salary": [50000,40000,60000,70000,45000]
}

df = pd.DataFrame(data)
print("Employee Dataset")
print(df)

print("\n Average Salary By department")
print(df.groupby("Department")["Salary"].mean())

print("\nHighest salary department ")
print(df.groupby("Department")["Salary"].max().idxmax())

print("\nTotal salary expense")
print(df["Salary"].sum())

