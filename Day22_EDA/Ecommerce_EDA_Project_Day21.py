# ==========================================================
# E-COMMERCE SALES EXPLORATORY DATA ANALYSIS (Day 21)
# ==========================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "Product":["Laptop","Phone","Tablet","Mouse","Keyboard","Laptop","Phone","Tablet","Mouse","Keyboard"],
    "Category":["Electronics","Electronics","Electronics","Accessories","Accessories","Electronics","Electronics","Electronics","Accessories","Accessories"],
    "Price":[50000,25000,18000,800,1500,50000,25000,18000,800,1500],
    "Quantity":[5,8,4,20,15,3,5,2,10,8],
    "Rating":[4.5,4.2,4.1,3.8,4.0,4.6,4.3,4.0,3.9,4.1],
    "City":["Delhi","Mumbai","Delhi","Lucknow","Delhi","Mumbai","Delhi","Lucknow","Delhi","Mumbai"]
}

df = pd.DataFrame(data)
df["Revenue"] = df["Price"] * df["Quantity"]

print("="*60)
print("E-COMMERCE SALES EDA")
print("="*60)
print(df)

print("\nShape:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nInfo:")
df.info()
print("\nDescribe:\n", df.describe())
print("\nMissing Values:\n", df.isnull().sum())
print("\nDuplicate Rows:", df.duplicated().sum())

print("\nMost Expensive Product:\n", df.loc[df["Price"].idxmax()])
print("\nCheapest Product:\n", df.loc[df["Price"].idxmin()])
print("\nHighest Revenue Product:\n", df.loc[df["Revenue"].idxmax()])
print("\nBest Rated Product:\n", df.loc[df["Rating"].idxmax()])

print("\nTotal Revenue:", df["Revenue"].sum())
print("Average Revenue:", round(df["Revenue"].mean(),2))
print("Average Rating:", round(df["Rating"].mean(),2))

print("\nRevenue by Category:\n", df.groupby("Category")["Revenue"].sum())
print("\nRevenue by City:\n", df.groupby("City")["Revenue"].sum())
print("\nRevenue by Product:\n", df.groupby("Product")["Revenue"].sum().sort_values(ascending=False))
print("\nCorrelation:\n", df.corr(numeric_only=True))

plt.figure(figsize=(6,4))
plt.hist(df["Price"])
plt.title("Price Distribution")
plt.show()

plt.figure(figsize=(8,5))
p = df.groupby("Product")["Revenue"].sum()
plt.bar(p.index, p.values)
plt.title("Revenue by Product")
plt.show()

plt.figure(figsize=(6,6))
c = df.groupby("Category")["Revenue"].sum()
plt.pie(c.values, labels=c.index, autopct="%1.1f%%")
plt.title("Revenue Share by Category")
plt.show()

plt.figure(figsize=(6,4))
sns.boxplot(x=df["Price"])
plt.title("Price Boxplot")
plt.show()

plt.figure(figsize=(6,5))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="Blues")
plt.title("Correlation Heatmap")
plt.show()

print("\nBest Category:", c.idxmax())
print("Best City:", df.groupby("City")["Revenue"].sum().idxmax())
print("="*60)
print("EDA COMPLETED SUCCESSFULLY")
print("="*60)
