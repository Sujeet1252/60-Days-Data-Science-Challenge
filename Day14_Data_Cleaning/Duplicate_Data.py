#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

data = {
    "Name": ["Aman", "Rahul", "Aman"],
    "Salary": [50000, 60000, 50000]
}

df = pd.DataFrame(data)
print(df)


# In[3]:


# Find Duplicates

print(df.duplicated())


# In[5]:


#Removes Duplicated

df = df.drop_duplicates()
print(df)

