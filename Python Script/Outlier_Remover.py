#!/usr/bin/env python
# coding: utf-8

# # Outlier Remover
# IQR Method

# In[3]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[5]:


data = sns.load_dataset("tips")
data.head()


# In[6]:


data.describe()


# In[37]:


plt.figure(figsize= (10,5))
sns.boxplot(x=data["total_bill"])
plt.title("Box plot of Total bill")
plt.show()


# In[32]:


Q1 = data["total_bill"].quantile(0.25)
Q3 = data["total_bill"].quantile(0.75)

IQR = Q3-Q1

lower = Q1-1.5 * IQR
upper = Q3+1.5 * IQR

print("Lower Limit " , lower)
print("Upper Limit ", upper)


# In[33]:


data.shape


# In[34]:


new_data =data[(data["total_bill"]<=upper) & (data["total_bill"]>=lower)]
new_data.shape


# In[36]:


plt.figure(figsize= (10,5))
sns.boxplot(x=new_data["total_bill"])
plt.title("Box plot of Total bill")
plt.show()


# In[ ]:




