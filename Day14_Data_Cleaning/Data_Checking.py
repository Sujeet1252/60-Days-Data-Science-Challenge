#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np

data = {
    "Name": ["Aman", "Rahul", None, "Priya", "Neha"],
    "Age": [23, np.nan, 25, 22, 23],
    "Salary": [50000, 60000, np.nan, 70000, 50000]
}

df = pd.DataFrame(data)

print(df)


# In[2]:


#Check Missing VAlues

print(df.isnull())


# In[3]:


#Count Missing VAlues

print(df.isnull().sum())


# In[4]:


#Removes rows containing missing Values

df.dropna()


# In[5]:


#Fill Age with Average

df["Age"] = df["Age"].fillna(df["Age"].mean())
print(df)


# In[6]:


#Fill Salary with Average

df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
print(df)


# In[7]:


#Fill Name with Unknown

df["Name"] = df["Name"].fillna("Unknown")
print(df)

