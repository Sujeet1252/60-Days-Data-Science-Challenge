#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

import numpy as np

data = {
    "Name":["Sujeet","Rohan","Mohit","Nitin","Rohan"],
    "Age" : [23,34,25,25,np.nan],
    "Salary": [25000,30000,np.nan,20000,25000]
}

df= pd.DataFrame(data)

print(df)


# In[3]:


print(df.isnull())


# In[4]:


print(df.isnull().sum())


# In[5]:


df["Age"] = df["Age"].fillna("27")
print(df)


# In[7]:


df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
print(df)


# In[ ]:




