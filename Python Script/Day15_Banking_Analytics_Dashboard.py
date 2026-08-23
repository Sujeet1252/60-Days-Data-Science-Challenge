#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd

data = {
    "Customer": [
        "Aman", "Rahul", "Priya", "Neha", "Rohit",
        "Simran", "Karan", "Anjali", "Vikas", "Pooja",
        "Arjun", "Sneha", "Raj", "Meera", "Akash"
    ],

    "Account_Type": [
        "Savings", "Current", "Savings", "Current", "Savings",
        "Current", "Savings", "Current", "Savings", "Savings",
        "Current", "Savings", "Current", "Savings", "Current"
    ],

    "Balance": [
        50000, 120000, 75000, 150000, 65000,
        200000, 90000, 110000, 45000, 85000,
        175000, 95000, 130000, 70000, 160000
    ],

    "City": [
        "Delhi", "Mumbai", "Delhi", "Bangalore", "Jaipur",
        "Mumbai", "Pune", "Delhi", "Jaipur", "Pune",
        "Bangalore", "Mumbai", "Delhi", "Pune", "Bangalore"
    ]
}

df = pd.DataFrame(data)
print("="*45)
print("        Banking Analytics Dashboard")
print("="*45)
print(df)

print("\n---- Total Customers ----")
print("Total Customers are : ", df["Customer"].count())

print("\n---- Total Balance ----")
print("Total Balance are : ",df["Balance"].sum())

print("\n---- Average balance ----")
print("Average Balance are : ", df["Balance"].mean())

print("\n---- Richest Customer ----")
print(df.loc[df["Balance"].idxmax()])

print("\n---- Balance By city ----")
print(df.groupby("City")["Balance"].sum())

print("\n----  Balance by Account Type ----")
print(df.groupby("Account_Type")["Balance"].sum())

print("\n")
print("="*45)
print("            End of Dashboard")
print("="*45)

