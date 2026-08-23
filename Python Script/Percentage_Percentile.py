#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


# In[14]:


dataset = sns.load_dataset("titanic")
dataset.head(5)


# In[25]:


dataset.describe()


# In[17]:


dataset["age"] = dataset['age'].fillna(dataset['age'].mean())


# In[23]:


print(np.percentile(dataset['age'],0) , np.percentile(dataset['age'],55))


# In[22]:


dataset['age'].median()


# In[ ]:




