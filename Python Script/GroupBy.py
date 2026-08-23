#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd

data = {
    "Department": ["IT", "HR", "IT", "HR", "Finance"],
    "Salary": [50000, 40000, 60000, 45000, 70000]
}

df = pd.DataFrame(data)
print("Average of Salary per Department")
print(df.groupby("Department")["Salary"].mean())

print("\n Sum of Salary per Department")
print(df.groupby("Department")["Salary"].sum())

print("\n Count Department Size")
print(df.groupby("Department").size())

