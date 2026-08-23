#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd

Employee = {
    "Name" : ["Sujeet","Ram","Sam","Rohan","Sumit"],
    "Salary" : [35000,25000,30000,32000,28000],
    "City" : ["Varanasi","dehradun","Delhi","Mumbai","Jaipur"],
    "Age" : [23,35,26,24,25]
}

df = pd.DataFrame(Employee)
print("== Employee Details ==")
print(df)

print("\n== Employee Salary More than 30000 ==")
print(df[df["Salary"]>30000])

print("\n== Employee from Delhi ==")
print(df[df["City"]=="Delhi"])

products = {
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Phone"],
    "Price": [55000, 500, 1200, 15000, 25000]
}

product_df = pd.DataFrame(products)

print("\n== Product Price ==")
print(product_df[product_df["Price"] > 1000])

customers = {
    "Name": ["Aman", "Rohit", "Suman", "Neha", "Priya"],
    "Age": [22, 28, 30, 24, 27]
}

customer_df = pd.DataFrame(customers)
print("\n== Customer Age ==")
print(customer_df[customer_df["Age"] > 25])



# In[ ]:




