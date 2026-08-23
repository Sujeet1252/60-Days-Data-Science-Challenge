#!/usr/bin/env python
# coding: utf-8

# # Outlier Remover
# Z Score Method

# In[2]:


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from scipy.stats import zscore


# In[3]:


data = sns.load_dataset("tips")
data.head()


# In[5]:


data["z_score"] = zscore(data["total_bill"])
data.head()


# In[6]:


outliers = data[(data["z_score"]>3) | (data["z_score"]<-3)]
outliers


# In[7]:


len(outliers)


# In[9]:


new_data = data[(data["z_score"]>= -3) & (data["z_score"]<=3)]
new_data.shape


# In[10]:


print("original Shape : ",data.shape)
print("After Removing : ", new_data.shape)


# In[11]:


plt.figure(figsize=(8,4))
sns.boxplot(x=data["total_bill"])
plt.title("Before Removing Outliers")
plt.show()


# In[13]:


plt.figure(figsize=(8,4))
sns.boxplot(x=new_data["total_bill"])
plt.title("After Removing Outliers")
plt.show()


# In[ ]:




