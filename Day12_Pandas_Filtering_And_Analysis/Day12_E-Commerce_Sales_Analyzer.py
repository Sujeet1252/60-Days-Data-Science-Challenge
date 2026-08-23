#!/usr/bin/env python
# coding: utf-8

# In[19]:


import pandas as pd

data = {
    "Product": ["Laptop", "Phone", "Tablet", "Mouse", "Keyboard"],
    "Price": [50000, 25000, 18000, 800, 1500],
    "Quantity": [5, 8, 4, 20, 15]
}

df = pd.DataFrame(data)

print("=" *40)
print("       E-Commerce Sales Analyzer   ")
print("=" *40)

print("\n==== Products Datasets ====")
print(df)

print("\n==== Total Revenue ====")
df["total_revenue"] = df["Price"] * df["Quantity"]
print(df["total_revenue"].sum())

print("\n==== Best Selling Products ====")
print(df.loc[df["Quantity"].idxmax()])

print("\n==== Most Expensive Products ====")
print(df.loc[df["Price"].idxmax()])

print("\n==== Cheapest Products ====")
print(df.loc[df["Price"].idxmin()])


print("\n==== Top 3 Revenue Generating Products ====")
top_revenue = df.sort_values(
    by="total_revenue",
    ascending=False
).head(3)

print(top_revenue[["Product", "total_revenue"]])

