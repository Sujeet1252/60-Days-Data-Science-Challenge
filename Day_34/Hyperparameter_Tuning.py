#!/usr/bin/env python
# coding: utf-8

# # Hyperparameter Tuning

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


data = pd.read_csv("Ice_cream selling data (1).csv")
data.head()


# In[4]:


X = data[["Temperature (°C)"]]
y = data["Ice Cream Sales (units)"]


# In[5]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# In[6]:


from sklearn.tree import DecisionTreeRegressor


# In[20]:


dt = DecisionTreeRegressor(criterion="poisson",max_depth =5,splitter= "best")
dt.fit(X_train,y_train)


# In[21]:


dt.score(X_train,y_train)*100


# In[22]:


dt.score(X_test,y_test)*100


# In[23]:


from sklearn.model_selection import GridSearchCV , RandomizedSearchCV


# In[24]:


df = {"criterion": ["squared_error", "absolute_error", "poisson"],
     "splitter":["best","random"],
     "max_depth":[i for i in range(2,20)]
}


# In[25]:


gd = GridSearchCV(DecisionTreeRegressor(),param_grid=df,cv=5)
gd.fit(X_train,y_train)


# In[26]:


gd.best_params_


# In[27]:


gd.best_score_


# In[28]:


rd = RandomizedSearchCV(DecisionTreeRegressor(),param_distributions=df,n_iter =20)
rd.fit(X_train,y_train)


# In[29]:


rd.best_params_


# In[30]:


rd.best_score_


# In[ ]:




