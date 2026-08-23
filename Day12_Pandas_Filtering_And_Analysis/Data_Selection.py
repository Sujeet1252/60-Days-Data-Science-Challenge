#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd


Employee = {
    "Name" : ["Sujeet","Ram","Sam","Rohan","Sumit"],
    "Salary" : [35000,25000,30000,32000,28000],
    "City" : ["Varanasi","dehradun","Delhi","Mumbai","Jaipur"]
}

df = pd.DataFrame(Employee)

print(df)

print("\n== Display Name Column ==")
print(df["Name"])

print("\n== Display Salary Column ==")
print(df["Salary"])

print("\n== Display Multiple Columns ==")
print(df[["Name","Salary"]])

print("\n== Display First Three rows ==")

