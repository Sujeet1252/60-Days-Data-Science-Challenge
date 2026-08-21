#!/usr/bin/env python
# coding: utf-8

# # Bagging Regressor

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


dataset = pd.read_csv("placement.csv")
dataset.head()


# In[3]:


x = dataset.iloc[:,:-1]
y = dataset["package"]


# In[4]:


from sklearn.model_selection import train_test_split

x_train , x_test , y_train , y_test = train_test_split(
    x,
    y,
    random_state=42,
    test_size=0.2
)


# In[ ]:





# In[6]:


from sklearn.ensemble import BaggingRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression


# In[12]:


bg = BaggingRegressor(estimator=LinearRegression(),n_estimators=100)
bg.fit(x_train,y_train)


# In[13]:


bg.score(x_train,y_train)*100 , bg.score(x_test,y_test)*100


# In[ ]:





# In[ ]:





# In[17]:


rf = RandomForestRegressor(n_estimators=10)
rf.fit(x_train,y_train)


# In[18]:


rf.score(x_train,y_train)*100 , rf.score(x_test,y_test)*100


# In[ ]:




