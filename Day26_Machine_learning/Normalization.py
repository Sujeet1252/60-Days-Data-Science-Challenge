#!/usr/bin/env python
# coding: utf-8

# # Feature Scaling
# Normalization

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


# In[2]:


dataset  = sns.load_dataset("titanic")
dataset.head()


# In[3]:


dataset["age"] = dataset["age"].fillna(dataset["age"].mean())
dataset["age"].isnull().sum()


# In[4]:


sns.histplot(dataset["age"],kde= True)
plt.show()


# In[7]:


from sklearn.preprocessing import MinMaxScaler


# In[8]:


ms = MinMaxScaler()
ms.fit(dataset[["age"]])


# In[9]:


dataset["age ms"] = pd.DataFrame(ms.transform(dataset[["age"]]),columns=["x"])
dataset.head(3)


# In[10]:


plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
plt.title("Before Scaling")
sns.histplot(dataset["age"],kde=True)

plt.subplot(1,2,2)
plt.title("After Scaling")
sns.histplot(dataset["age ms"],kde= True)

plt.show()


# In[ ]:




