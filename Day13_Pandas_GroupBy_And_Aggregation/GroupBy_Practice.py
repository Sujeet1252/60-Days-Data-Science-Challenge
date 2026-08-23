#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd

employee = {
    "Name": ["Sujeet", "Ram", "Rohan", "Aman", "Priya", "Sumit"],
    "Department": ["IT", "HR", "IT", "Finance", "HR", "Finance"],
    "Salary": [50000, 30000, 60000, 55000, 35000, 65000]
}

df = pd.DataFrame(employee)

print(df)

print("\n Employees by Department ")

print(df.groupby("Department")["Name"].apply(list))

for dept, data in df.groupby("Department"):
    print(f"\nDepartment : {dept}")
    print(data)

print("\n Average Salary per Departmnet")
print(df.groupby("Department")["Salary"].mean())

print("\nMaximum Salary Per Department")
print(df.groupby("Department")["Salary"].max())

print("\nMinimum Salary Per Department")
print(df.groupby("Department")["Salary"].min())

print("\nTotal Salary Per Department")
print(df.groupby("Department")["Salary"].sum())

