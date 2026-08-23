#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = sns.load_dataset("titanic")
df


# In[6]:


mode = df["fare"].mode()[0]
print("Mode is : ",mode)
df["fare"].value_counts()


# In[7]:


sns.histplot(x= "fare",data=df,bins=[i for i in range(0,80,10)])
plt.plot([mode for i in range(0,300)], [i for i in range(0,300)],c="red")
plt.show()


# In[ ]:




