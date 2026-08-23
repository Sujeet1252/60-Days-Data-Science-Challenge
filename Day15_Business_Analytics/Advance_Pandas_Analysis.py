#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

data = {
    "Product": [
        "Laptop", "Phone", "Tablet", "Mouse", "Keyboard",
        "Monitor", "Printer", "Laptop", "Phone", "Tablet"
    ],

    "Category": [
        "Electronics", "Electronics", "Electronics",
        "Accessories", "Accessories",
        "Electronics", "Office", "Electronics",
        "Electronics", "Electronics"
    ],

    "City": [
        "Delhi", "Mumbai", "Delhi", "Lucknow", "Mumbai",
        "Delhi", "Jaipur", "Lucknow", "Jaipur", "Mumbai"
    ],

    "Customer": [
        "Aman", "Rahul", "Priya", "Neha", "Rohit",
        "Simran", "Karan", "Pooja", "Vikas", "Anjali"
    ],

    "Price": [
        50000, 25000, 18000, 800, 1500,
        12000, 10000, 50000, 25000, 18000
    ],

    "Quantity": [
        5, 8, 4, 20, 15,
        6, 3, 2, 7, 5
    ]
}

df = pd.DataFrame(data)

print(df)


# In[2]:


# Revenue Calculations

df["Revenue"]= df["Price"] * df["Quantity"]
print(df)


# In[3]:


#Total Revenue

print("Total Revenue is : ", df["Revenue"].sum())


# In[4]:


#Top Products

print(df.sort_values(by="Revenue",ascending= False))


# In[5]:


#Top 3 Products

print(df.sort_values(by = "Revenue", ascending = False).head(3))


# In[7]:


#Category Analysis

print(df.groupby("Category")["Revenue"].sum())


# In[8]:


#City Wise Sales

print(df.groupby("City")["Revenue"].sum())


# In[9]:


#Top Customers

print(df.groupby("Customer")["Revenue"].sum().sort_values(ascending=False).head(3)
     )


# In[10]:


# Best Selling Product (By Quantity)

print(
    df.groupby("Product")["Quantity"]
      .sum()
      .sort_values(ascending=False)
)


# In[11]:


#Most Expensive Product

print(
    df.loc[df["Price"].idxmax()]
)


# In[13]:


#Cheapest Product

print(
    df.loc[df["Price"].idxmin()]
)


# In[ ]:




