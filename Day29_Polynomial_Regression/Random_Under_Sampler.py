#!/usr/bin/env python
# coding: utf-8

# # Techniques To Handle Imbalance Data
# 
# Random Under Sampling

# In[1]:


import pandas as pd


# In[2]:


dataset = pd.read_csv("Social_Network_Ads.csv")
dataset.head()


# In[3]:


dataset.isnull().sum()


# In[4]:


dataset["Purchased"].value_counts()


# In[5]:


x = dataset[["Age","EstimatedSalary"]]
y = dataset["Purchased"]


# In[6]:


from sklearn.model_selection import train_test_split

x_train , x_test , y_train , y_test = train_test_split(
    x,
    y,
    random_state = 42,
    test_size = 0.2
)


# In[7]:


print(x_train.shape)
print(y_train.shape)


# In[8]:


from imblearn.under_sampling import RandomUnderSampler

rus = RandomUnderSampler(random_state=42)

x_train, y_train = rus.fit_resample(x_train, y_train)


# In[9]:


print(x_train.shape)
print(y_train.shape)
print(y_train.value_counts())


# In[10]:


from sklearn.linear_model import LogisticRegression

lr = LogisticRegression()
lr.fit(x_train, y_train)


# In[11]:


lr.score(x_test , y_test) * 100


# In[14]:


lr.predict([[30,135000]])


# In[ ]:




