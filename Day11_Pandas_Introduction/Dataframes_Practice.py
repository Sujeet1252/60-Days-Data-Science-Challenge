#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd

Students_data = {
    "Names" : ["Sujeet","Ram","Sam","Rohit","Roy","Joy","Rock"],
    "Marks" : [95,85,74,56,85,45,74]
}
df = pd.DataFrame(Students_data)

print("=== Display Student DataFrame ===")
print(df)

print("\n=== Display Names Column ===")
print(df["Names"])


print("\n=== Display Marks Column ===")
print(df["Marks"])

print("\n=== Display Multiple Columns ===")
print(df[["Marks" , "Names"]])

