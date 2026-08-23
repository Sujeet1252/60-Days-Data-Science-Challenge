#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

data = {
    "Name": ["Sujeet", "Rahul", "Aman"],
    "Marks": [90, 85, 88]
}

df = pd.DataFrame(data)

print(df)

