#!/usr/bin/env python
# coding: utf-8

# In[19]:


import pandas as pd

employees = {
    "Name": ["Aman","Rahul","Priya","Neha","Rohit","Simran","Karan"],
    "Department": ["IT","HR","IT","Finance","HR","Finance","IT"],
    "Salary": [50000,40000,60000,70000,45000,80000,55000],
    "Experience": [2,1,4,6,3,8,5]
}

df = pd.DataFrame(employees)

print("="*40)
print("    Employee Analytics Dashboard")
print("="*40)

print("\n== Employee Datasets ==")
print(df)

print("\n=== Total Employeees ===")
print("Total Employees is :",df["Name"].count())

print("Average Salary is :",df["Salary"].mean())
print("Highest Salary is :",df["Salary"].max())
print("Lowest Salary is : ",df["Salary"].min())

print("\n=== Average Salary by Department ===")
print(df.groupby("Department")["Salary"].mean())

print("\n=== Total Salary by Department ===")
print(df.groupby("Department")["Salary"].sum())

print("\n=== Employee Count by Department ===")
print(df.groupby("Department")["Name"].count())

print("\n=== Most Experienced Employee ===")
print(df.loc[df["Experience"].idxmax()])

print("\n=== Average Experience ===")
print(df["Experience"].mean())

print("\n=== Highest Paid Employee ===")
print(df.loc[df["Salary"].idxmax()])

print("\n===Top 3 Salaries ===")
print(df.nlargest(3,"Salary"))

