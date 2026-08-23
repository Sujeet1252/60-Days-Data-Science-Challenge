#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd

Data = {
    "Product" : ["Laptop", "Mouse", "Phone", "Tablet"],
    "Price"   : [50000,800,25000,18000] 
}

df = pd.DataFrame(Data)
print("\n== Product dataset ==")
print(df)

print("\n== Most Expensive product ==")
print(df.loc[df["Price"].idxmax()])

print("\n== Cheapest Product ==")
print(df.loc[df["Price"].idxmin()])

print("\n== Products above ₹10,000 ==")
print(df.loc[df["Price"]>10000])

