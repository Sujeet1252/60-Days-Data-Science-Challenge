#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


# In[2]:


sec_a = np.array([45,34,56,67,78,34])
sec_b = np.array([23,45,64,35,46,76])
no = np.array([1,2,3,4,5,6])


# In[3]:


#Standard Deviation

np.std(sec_a) , np.std(sec_b)


# In[4]:


#VAriance i.e. square of standard Deviation

np.var(sec_a), np.var(sec_b)


# In[5]:


data = sns.load_dataset("titanic")
data


# In[6]:


data['age'].var()


# In[10]:


data.describe()


# In[9]:


sns.histplot(x = "age", data = data)
plt.show()


# In[ ]:




