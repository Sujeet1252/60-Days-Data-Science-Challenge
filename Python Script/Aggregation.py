#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd

employee = {
    "Name": ["Sujeet", "Ram", "Rohan", "Aman", "Priya", "Sumit"],
    "Department": ["IT", "HR", "IT", "Finance", "HR", "Finance"],
    "Salary": [50000, 30000, 60000, 55000, 35000, 65000]
}

df = pd.DataFrame(employee)

print("Employee Dataset")
print(df)

print("\n== Employee Count ==")
print(df.groupby("Department")["Name"].count())

print("\n== Multiple Statistics ==")
print(df.groupby("Department")["Salary"].agg(["count","sum","mean","max","min"]))

print("\n== Sorted by Average Salary ==")
print(df.groupby("Department")["Salary"].mean().sort_values(ascending=False))

print("\nDepartment with Highest Salary:")
print(df.groupby("Department")["Salary"].max().idxmax())

print("\nDepartment with Most Employees:")
print(df.groupby("Department")["Name"].count().idxmax())

