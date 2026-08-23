#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np

data = {
    "Patient": [
        "Aman", "Rahul", "Priya", "Neha", "Rohit",
        "Simran", "Karan", "Pooja", "Vikas", "Anjali"
    ],

    "Age": [
        25, 32, np.nan, 41, 28,
        35, 50, np.nan, 45, 30
    ],

    "Disease": [
        "Fever", "Diabetes", "Asthma", "BP", "Fever",
        "Cancer", "Diabetes", "Asthma", "BP", "Fever"
    ],

    "Bill": [
        5000, 12000, 8000, np.nan, 4500,
        50000, 15000, 9000, np.nan, 5000
    ]
}

df = pd.DataFrame(data)

# Add duplicate row
df = pd.concat([df, df.iloc[[1]]], ignore_index=True)

print("=== Dirty Healthcare Dataset ===")
print(df)

print("\n=== Missing Values ===")
print(df.isnull().sum())

avg_age = df["Age"].mean()
df["Age"] = df["Age"].fillna(avg_age)
print("\nAverage Age:", avg_age)

avg_bill = df["Bill"].mean()
df["Bill"] = df["Bill"].fillna(avg_bill)
print("\nAverage Bill:", avg_bill)

print("\n=== Duplicate Rows ===")
print(df[df.duplicated()])

df = df.drop_duplicates()
print("\n=== Dataset After Removing Duplicates ===")
print(df)

print("\n" + "="*50)
print("HEALTHCARE DATA CLEANING REPORT")
print("="*50)

print("Total Patients :", len(df))

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nAverage Age:")
print(df["Age"].mean())

print("\nAverage Bill:")
print(df["Bill"].mean())

print("\nHighest Bill:")
print(df["Bill"].max())

print("\nLowest Bill:")
print(df["Bill"].min())

print("\nFinal Clean Dataset:")
print(df)

