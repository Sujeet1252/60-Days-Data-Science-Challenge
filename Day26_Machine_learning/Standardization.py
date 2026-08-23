#!/usr/bin/env python
# coding: utf-8

# # Feature Scaling Technique
# Standardization

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


# In[9]:


dataset  = sns.load_dataset("titanic")
dataset.head()


# In[10]:


dataset.isnull().sum()


# In[11]:


dataset["age"] = dataset["age"].fillna(dataset["age"].mean())
dataset["age"].isnull().sum()


# In[13]:


sns.histplot(dataset["age"],kde= True)
plt.show()


# In[14]:


dataset.describe()


# In[15]:


from sklearn.preprocessing import StandardScaler


# In[16]:


ss = StandardScaler()
ss.fit(dataset[["age"]])


# In[17]:


dataset["age ss"] = pd.DataFrame(ss.transform(dataset[["age"]]),columns=["x"])


# In[18]:


dataset.head()


# In[25]:


plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
plt.title("Before Scaling")
sns.histplot(dataset["age"],kde=True)

plt.subplot(1,2,2)
plt.title("After Scaling")
sns.histplot(dataset["age ss"],kde= True)

plt.show()


# In[23]:


print(dataset["age"].mean())
print(dataset["age ss"].mean())


# In[24]:


print(dataset["age"].std())
print(dataset["age ss"].std())


# In[ ]:




