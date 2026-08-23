#!/usr/bin/env python
# coding: utf-8

# # Outlier

# In[5]:


import numpy  as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


# In[6]:


data = sns.load_dataset("tips")
data


# In[7]:


sns.boxplot(x="total_bill", data= data)
plt.show()


# In[9]:


sns.distplot(data["total_bill"])
plt.show()


# In[ ]:




