#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

data = {
    "Product": [
        "Laptop",
        "Phone",
        "Tablet",
        "Mouse",
        "Keyboard",
        "Laptop",
        "Phone",
        "Tablet"
    ],

    "Category": [
        "Electronics",
        "Electronics",
        "Electronics",
        "Accessories",
        "Accessories",
        "Electronics",
        "Electronics",
        "Electronics"
    ],

    "Price": [
        50000,
        25000,
        18000,
        800,
        1500,
        50000,
        25000,
        18000
    ],

    "Quantity": [
        5,
        8,
        4,
        20,
        15,
        3,
        5,
        2
    ],

    "City": [
        "Delhi",
        "Mumbai",
        "Delhi",
        "Lucknow",
        "Delhi",
        "Mumbai",
        "Delhi",
        "Lucknow"
    ]
}

df = pd.DataFrame(data)

print("=="*27)
print("       E-Commerce Business Analytics Dashboard")
print("=="*27)
print(df)

df["Revenue"] = df["Price"] * df["Quantity"]

total_revenue = df["Revenue"].sum()

total_orders = len(df)

average_revenue = df["Revenue"].mean()

highest_revenue = df["Revenue"].max()

lowest_revenue = df["Revenue"].min()

print("\n===== BUSINESS KPIs =====")

print("Total Revenue       : ₹",total_revenue)
print("Total Orders        :",total_orders)
print("Average Revenue     : ₹", round(average_revenue, 2))
print("Highest Revenue     : ₹", highest_revenue)
print("Lowest Revenue      : ₹", lowest_revenue)


top_product = df.loc[df["Revenue"].idxmax()]
print("\n===== TOP PRODUCT =====")

print("Product :", top_product["Product"])
print("Revenue : ₹", top_product["Revenue"])


print("\n===== TOP 3 PRODUCTS =====")

top3 = df.sort_values(
    by="Revenue",
    ascending=False
).head(3)
print(top3[["Product", "Revenue"]])

category_revenue = df.groupby(
    "Category"
)["Revenue"].sum()
print("\n===== CATEGORY ANALYSIS =====")
print(category_revenue)

best_category = category_revenue.idxmax()
print("\nBest Category :", best_category)

city_revenue = df.groupby(
    "City"
)["Revenue"].sum()
print("\n===== CITY ANALYSIS =====")
print(city_revenue)

best_city = city_revenue.idxmax()
print("\nBest City :", best_city)

product_sales = df.groupby(
    "Product"
)["Quantity"].sum()
print("\n===== PRODUCT SALES =====")
print(product_sales.sort_values(
    ascending=False
))

print("\n===== REVENUE RANKING =====")
ranking = df.groupby(
    "Product"
)["Revenue"].sum()
print(
    ranking.sort_values(
        ascending=False
    )
)

print("=="*27)
print("                 End Of Dashboard")
print("=="*27)

