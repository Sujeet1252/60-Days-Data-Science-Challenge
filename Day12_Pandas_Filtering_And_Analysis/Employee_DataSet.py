#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd

Employee = {
    "Name" : ["Aman","Rahul","Priya"],
    "Salary": [45000,65000,55000]
}

df= pd.DataFrame(Employee)

print(df)

print("\n== Highest Salary ==")
print(df.loc[df["Salary"].idxmax()])

print("\n== Average Salary ==")
avg = df["Salary"].mean()
print(avg)

print("\n ==Employees earning above average ==")
print(df[df["Salary"]>avg])

