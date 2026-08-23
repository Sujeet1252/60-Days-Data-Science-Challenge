#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[3]:


data = sns.load_dataset("titanic")
data


# In[19]:


sns.barplot(x = data.sex,y = data.age,color="r",palette = 'icefire', saturation=10,capsize=0.5,errcolor="b")
plt.show()


# In[ ]:




