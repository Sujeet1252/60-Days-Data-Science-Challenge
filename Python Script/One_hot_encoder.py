#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns


# In[2]:


dataset = sns.load_dataset("titanic")
dataset.head()


# In[6]:


dataset.isnull().sum()


# In[5]:


dataset["age"] = dataset["age"].fillna(dataset["age"].mean())


# In[8]:


data = dataset["sex"]
pd.get_dummies(data)


# In[12]:


from sklearn.preprocessing import OneHotEncoder
ohe = OneHotEncoder(sparse_output=False)
encoded = ohe.fit_transform(dataset[["sex"]])
encoded


# In[13]:


encoded_df = pd.DataFrame(encoded,columns = ohe.get_feature_names_out(['sex']))
encoded_df.head()


# In[15]:


pd.get_dummies(dataset,columns=["sex"])

