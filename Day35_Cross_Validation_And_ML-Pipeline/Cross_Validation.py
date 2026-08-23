#!/usr/bin/env python
# coding: utf-8

# # Cross Validation in Machine Learning

# In[2]:


import pandas as pd


# In[3]:


data = pd.read_csv("placement.csv")
data.head(3)


# In[4]:


data.shape


# In[5]:


x = data[["cgpa"]]
y = data["package"]


# In[6]:


df = data.head(5)


# In[7]:


x_new = df[["cgpa"]]
y_new = df["package"]


# In[8]:


from sklearn.model_selection import KFold , LeaveOneOut , LeavePOut


# In[9]:


lo =  LeaveOneOut()
for train , test in lo.split(x_new,y_new):
    print(train,test)


# In[10]:


lpo =  LeavePOut(p=2)
for train , test in lpo.split(x_new,y_new):
    print(train,test)


# In[11]:


kf = KFold(n_splits=3)
for train , test in kf.split(x_new,y_new):
    print(train,test)


# In[12]:


from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score

p = cross_val_score(LinearRegression(),x,y,cv=5)


# In[13]:


p.sort()


# In[15]:


print(p*100)


# In[ ]:




