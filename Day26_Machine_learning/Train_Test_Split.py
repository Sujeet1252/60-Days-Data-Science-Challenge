#!/usr/bin/env python
# coding: utf-8

# # Train Test Split

# In[1]:


import pandas as pd


# In[3]:


dataset = pd.read_csv("loan_approval_dataset.csv")
dataset.head()


# In[17]:


dataset.info()


# In[18]:


dataset.shape


# In[5]:


input_data = dataset.iloc[:,:-1]
output_data = dataset[" loan_status"]


# In[6]:


from sklearn.model_selection import train_test_split


# In[8]:


x_train , x_test, y_train , y_test = train_test_split(input_data,output_data,test_size=0.25)


# In[21]:


x_train.head()


# In[25]:


x_test.shape , y_test.shape


# In[ ]:




