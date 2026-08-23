#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd

data = {
    "Product": [
        "Laptop", "Phone", "Tablet", "Mouse", "Keyboard",
        "Monitor", "Printer", "Headphones", "Speaker", "Camera"
    ],

    "Category": [
        "Electronics", "Electronics", "Electronics", "Accessories",
        "Accessories", "Electronics", "Office", "Accessories",
        "Accessories", "Electronics"
    ],

    "Price": [
        50000, 25000, 18000, 800, 1500,
        12000, 10000, 2500, 3500, 40000
    ],

    "Quantity": [
        5, 8, 4, 20, 15,
        6, 3, 10, 7, 2
    ]
}

df = pd.DataFrame(data)
print(" Sales Data ")
print(df)


df["Revenue"] = df["Quantity"] * df["Price"]
print("\n Calculate Revenue")
print(df[["Product","Revenue"]])

print("\nHighest Revenue Product")
print(df.loc[df["Revenue"].idxmax()])

print("\nLowest Revenue Product")
print(df.loc[df["Revenue"].idxmin()])

print("\nTotal Revenue")
print("Total revenue generated are : ", df["Revenue"].sum())

print("\nAverage Revenue")
print("Average Revenue =", df["Revenue"].mean())

