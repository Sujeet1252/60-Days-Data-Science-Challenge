#!/usr/bin/env python
# coding: utf-8

# # Feature Selection Technique
# Forward Elimination

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[24]:


dataset = sns.load_dataset("titanic")
dataset.head()


# In[26]:


x = dataset.iloc[:,:-1]
y = dataset["survived"]


# In[27]:


x.shape


# In[28]:


from mlxtend.feature_selection import SequentialFeatureSelector


# In[29]:


from sklearn.linear_model import LogisticRegression


# In[30]:


lr = LogisticRegression()


# In[32]:


fs = SequentialFeatureSelector(lr,k_features=14,forward =True)
fs.fit(x,y)


# In[ ]:




