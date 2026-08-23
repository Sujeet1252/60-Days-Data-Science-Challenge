#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import numpy as np

data = {
    "Product": [
        "Laptop",
        "Phone",
        None,
        "Laptop",
        "Tablet"
    ],

    "Price": [
        50000,
        np.nan,
        25000,
        50000,
        18000
    ],

    "Category": [
        "Electronics",
        "Electronics",
        None,
        "Electronics",
        "Electronics"
    ]
}

df = pd.DataFrame(data)

print("==" * 20)
print("    E-Commerce Data Cleaning System")
print("==" *20)
print(df)

print("\n Detect Missing Values")
print(df.isnull())

print("\n Fill Missing Product Name")
df["Product"]= df["Product"].fillna("Unknown Product")
print(df)

print("Fill Missing Price")
df["Price"] = df["Price"].fillna(df["Price"].mean())
print(df)

print("\n Fill Missing Category")
df["Category"] = df["Category"].fillna("Unknown Category")

print("\nRemove Duplicates")
print(df.drop_duplicates())

