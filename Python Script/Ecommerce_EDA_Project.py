#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[23]:


import pandas as pd

data = {
    "Product": [
        "Laptop","Phone","Tablet","Mouse",
        "Keyboard","Laptop","Phone","Tablet",
        "Mouse","Keyboard"
    ],

    "Category": [
        "Electronics","Electronics","Electronics",
        "Accessories","Accessories",
        "Electronics","Electronics","Electronics",
        "Accessories","Accessories"
    ],

    "Price": [
        50000,25000,18000,800,1500,
        50000,25000,18000,800,1500
    ],

    "Quantity": [
        5,8,4,20,15,
        3,5,2,7,8
    ],

    "Rating": [
        4.5,4.2,4.1,3.8,4.0,
        4.6,4.3,4.0,3.9,4.1
    ],

    "City": [
        "Delhi","Mumbai","Delhi","Lucknow","Delhi",
        "Mumbai","Delhi","Lucknow","Delhi","Mumbai"
    ]
}

df = pd.DataFrame(data)
print(df)


# In[24]:


df.shape


# In[25]:


df.columns


# In[26]:


df.info()


# In[27]:


df.describe()


# In[28]:


df.isnull().sum()


# In[29]:


df.duplicated().sum()


# In[30]:


df["Revenue"] = df["Price"] * df["Quantity"]
print("Total Revenue is :" , df["Revenue"].sum())
print("Average Revenue is :" , df["Revenue"].mean())


# In[31]:


print("Most Expensive Product is :")
df.loc[df["Price"].idxmax()]


# In[32]:


print("Highest Revenue Product is :")
df.loc[df["Revenue"].idxmax()]


# In[41]:


print("Revenue by category :")
print(df.groupby("Category")["Revenue"].sum())
print("\nRevenue by city :")
print(df.groupby("City")["Revenue"].sum())


# In[48]:


plt.hist(df["Price"],bins=5,color="skyblue",edgecolor="black")
plt.title("Price Distribution")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.grid(axis="y",alpha=0.7)
plt.show()


# In[49]:


df.groupby("Product")["Revenue"].sum().plot(kind="bar")


# In[50]:


sns.boxplot(x=df["Price"])


# In[51]:


sns.heatmap(df.corr(numeric_only=True),
           annot = True)


# In[ ]:




