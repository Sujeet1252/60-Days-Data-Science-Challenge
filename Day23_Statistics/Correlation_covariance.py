#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[5]:


dataset = sns.load_dataset("tips")
dataset


# In[6]:


dataset.isnull().sum()


# In[7]:


dataset.info()


# In[12]:


data_corr = dataset.select_dtypes(("float64","int64")).corr()
data_corr


# In[13]:


data_cov = dataset.select_dtypes(("float64","int64")).cov()
data_cov


# In[15]:


# Correlation

plt.figure(figsize=(4,3))
sns.heatmap(data_corr, annot =True)
plt.show()


# In[16]:


# Covariance

plt.figure(figsize=(4,3))
sns.heatmap(data_cov, annot =True)
plt.show()


# In[ ]:




