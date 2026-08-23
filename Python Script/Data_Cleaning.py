#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np

students = {
    "Name": ["Sujeet", "Rahul", None, "Aman", "Rahul", "Mayank"],
    "Marks": [85, 90, np.nan, 78, 90, 65],
    "City": ["Varanasi", "Delhi", "Lucknow", None, "Delhi", "Prayagraj"]
}

df = pd.DataFrame(students)

print(df)


# In[2]:


print(df.dropna())


# In[3]:


print(df.dropna(axis=1))


# In[4]:


duplicate_row = pd.DataFrame({
    "Name":["Rahul"],
    "Marks":[90],
    "City":["Delhi"]
})

df = pd.concat([df, duplicate_row], ignore_index=True)

print(df)


# In[5]:


print(df.duplicated())


# In[6]:


print(df.drop_duplicates())


# In[ ]:




