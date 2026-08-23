#!/usr/bin/env python
# coding: utf-8

# In[1]:


# ==========================================================
#        E-COMMERCE SALES EXPLORATORY DATA ANALYSIS
# ==========================================================

# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# Create Dataset
# -----------------------------
data = {
    "Product": [
        "Laptop", "Phone", "Tablet", "Mouse", "Keyboard",
        "Laptop", "Phone", "Tablet", "Mouse", "Keyboard"
    ],

    "Category": [
        "Electronics", "Electronics", "Electronics",
        "Accessories", "Accessories",
        "Electronics", "Electronics", "Electronics",
        "Accessories", "Accessories"
    ],

    "Price": [
        50000, 25000, 18000, 800, 1500,
        50000, 25000, 18000, 800, 1500
    ],

    "Quantity": [
        5, 8, 4, 20, 15,
        3, 5, 2, 10, 8
    ],

    "Rating": [
        4.5, 4.2, 4.1, 3.8, 4.0,
        4.6, 4.3, 4.0, 3.9, 4.1
    ],

    "City": [
        "Delhi", "Mumbai", "Delhi", "Lucknow", "Delhi",
        "Mumbai", "Delhi", "Lucknow", "Delhi", "Mumbai"
    ]
}

df = pd.DataFrame(data)

# -----------------------------
# Feature Engineering
# -----------------------------
df["Revenue"] = df["Price"] * df["Quantity"]

print("=" * 60)
print("         E-COMMERCE SALES DATASET")
print("=" * 60)

print(df)

# ==========================================================
# DATASET INSPECTION
# ==========================================================

print("\n" + "=" * 60)
print("DATASET INFORMATION")
print("=" * 60)

print("\nShape of Dataset:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nInformation:")
df.info()

print("\nStatistical Summary:")
print(df.describe())

# ==========================================================
# DATA CLEANING
# ==========================================================

print("\n" + "=" * 60)
print("DATA CLEANING")
print("=" * 60)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

# ==========================================================
# PRODUCT ANALYSIS
# ==========================================================

print("\n" + "=" * 60)
print("PRODUCT ANALYSIS")
print("=" * 60)

print("\nMost Expensive Product:")
print(df.loc[df["Price"].idxmax()])

print("\nCheapest Product:")
print(df.loc[df["Price"].idxmin()])

print("\nHighest Revenue Product:")
print(df.loc[df["Revenue"].idxmax()])

print("\nBest Rated Product:")
print(df.loc[df["Rating"].idxmax()])

# ==========================================================
# BUSINESS KPIs
# ==========================================================

print("\n" + "=" * 60)
print("BUSINESS KPIs")
print("=" * 60)

print("Total Products      :", len(df))

print("Total Revenue       :", df["Revenue"].sum())

print("Average Revenue     :", round(df["Revenue"].mean(),2))

print("Average Rating      :", round(df["Rating"].mean(),2))

print("Highest Price       :", df["Price"].max())

print("Lowest Price        :", df["Price"].min())

# ==========================================================
# CATEGORY ANALYSIS
# ==========================================================

print("\n" + "=" * 60)
print("CATEGORY ANALYSIS")
print("=" * 60)

print("\nRevenue by Category")
print(df.groupby("Category")["Revenue"].sum())

print("\nAverage Rating by Category")
print(df.groupby("Category")["Rating"].mean())

# ==========================================================
# CITY ANALYSIS
# ==========================================================

print("\n" + "=" * 60)
print("CITY ANALYSIS")
print("=" * 60)

print(df.groupby("City")["Revenue"].sum())

# ==========================================================
# PRODUCT REVENUE ANALYSIS
# ==========================================================

print("\n" + "=" * 60)
print("PRODUCT REVENUE")
print("=" * 60)

print(df.groupby("Product")["Revenue"].sum())

print("\nTop Revenue Products")

print(
    df.groupby("Product")["Revenue"]
      .sum()
      .sort_values(ascending=False)
)

# ==========================================================
# CORRELATION
# ==========================================================

print("\n" + "=" * 60)
print("CORRELATION MATRIX")
print("=" * 60)

print(df.corr(numeric_only=True))

# ==========================================================
# VISUALIZATION
# ==========================================================

# Histogram
plt.figure(figsize=(6,4))
plt.hist(df["Price"])
plt.title("Price Distribution")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.show()

# Bar Chart
plt.figure(figsize=(8,5))
product_revenue = df.groupby("Product")["Revenue"].sum()
plt.bar(product_revenue.index, product_revenue.values)
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.show()

# Pie Chart
plt.figure(figsize=(6,6))
category_revenue = df.groupby("Category")["Revenue"].sum()
plt.pie(
    category_revenue.values,
    labels=category_revenue.index,
    autopct="%1.1f%%"
)
plt.title("Revenue Share by Category")
plt.show()

# Boxplot
plt.figure(figsize=(6,4))
sns.boxplot(x=df["Price"])
plt.title("Price Boxplot")
plt.show()

# Heatmap
plt.figure(figsize=(6,5))
sns.heatmap(
    df.corr(numeric_only=True),
    annot=True,
    cmap="Blues"
)
plt.title("Correlation Heatmap")
plt.show()

# ==========================================================
# FINAL BUSINESS REPORT
# ==========================================================

print("\n" + "=" * 60)
print("FINAL BUSINESS REPORT")
print("=" * 60)

print("Total Revenue            :", df["Revenue"].sum())

print("Average Revenue          :", round(df["Revenue"].mean(),2))

print("Highest Revenue Product  :")
print(df.loc[df["Revenue"].idxmax()][["Product","Revenue"]])

print("\nMost Expensive Product")
print(df.loc[df["Price"].idxmax()][["Product","Price"]])

print("\nBest Rated Product")
print(df.loc[df["Rating"].idxmax()][["Product","Rating"]])

print("\nBest Category")
print(df.groupby("Category")["Revenue"].sum().idxmax())

print("\nBest Performing City")
print(df.groupby("City")["Revenue"].sum().idxmax())

print("=" * 60)
print("EDA COMPLETED SUCCESSFULLY")
print("=" * 60)


# In[ ]:




