#!/usr/bin/env python
# coding: utf-8

# # Machine Learning Basics

# In[4]:


import pandas as pd
import numpy as np
import kagglehub
import os 

path = kagglehub.dataset_download("architsharma01/loan-approval-prediction-dataset")

print("Path to dataset files:", path)
print(os.listdir(path))


# In[5]:


df = pd.read_csv(os.path.join(path,"loan_approval_dataset.csv"))
df.head()


# In[6]:


df.isnull().sum()


# In[12]:


df.info()


# In[13]:


df.select_dtypes(include="int64").columns


# In[14]:


from sklearn.impute import SimpleImputer


# In[16]:


si = SimpleImputer(strategy="mean")
ar =si.fit_transform(df[['loan_id', ' no_of_dependents', ' income_annum', ' loan_amount',
       ' loan_term', ' cibil_score', ' residential_assets_value',
       ' commercial_assets_value', ' luxury_assets_value',
       ' bank_asset_value']])


# In[19]:


new_dataset = pd.DataFrame(ar,columns = df.select_dtypes(include="int64").columns)


# In[21]:


new_dataset.head()


# In[27]:


df.columns.tolist()


# In[29]:


df[" loan_term"].mean()

