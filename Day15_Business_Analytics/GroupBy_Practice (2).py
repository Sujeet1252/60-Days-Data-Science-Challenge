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
        "Electronics", "Electronics", "Electronics",
        "Accessories", "Accessories",
        "Electronics", "Office",
        "Accessories", "Accessories", "Electronics"
    ],

    "Customer": [
        "Aman", "Rahul", "Priya", "Aman", "Rohit",
        "Rahul", "Priya", "Neha", "Aman", "Rohit"
    ],

    "City": [
        "Delhi", "Mumbai", "Delhi", "Jaipur", "Mumbai",
        "Delhi", "Pune", "Jaipur", "Delhi", "Pune"
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

# Revenue Column
df["Revenue"] = df["Price"] * df["Quantity"]

print(df)

print("\n Revenue by Category")
print("-"*25)
print(df.groupby("Category")["Revenue"].sum())

print("\n Revenue By City")
print("-"*25)
print(df.groupby("City")["Revenue"].sum())

print("\n Revenue by Customers")
print("-"*25)
print(df.groupby("Customer")["Revenue"].sum())

print("\nProduct count by category")
print("-"*25)
print(df.groupby("Category")["Product"].count())

print("\n Orders per City")
print("-"*25)
print(df.groupby("City")["Product"].count())

