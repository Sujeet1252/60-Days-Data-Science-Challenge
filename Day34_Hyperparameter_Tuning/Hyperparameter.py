#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

from sklearn.model_selection import (
train_test_split , GridSearchCV
) 


# In[2]:


from sklearn.neighbors import KNeighborsClassifier


# In[4]:


data = {
    "Age":[20,22,25,28,30,35,40,45,50,55],
    "Salary":[20000,25000,30000,35000,45000,50000,60000,70000,80000,90000],
    "Purchased":[0,0,0,0,1,1,1,1,1,1]
}

df = pd.DataFrame(data)
df


# In[5]:


x = df[["Age","Salary"]]

y = df["Purchased"]


# In[8]:


x_train , x_test, y_train  , y_test = train_test_split(
    x,
    y,
    random_state = 42,
    test_size = 0.2
)


# In[19]:


model = KNeighborsClassifier()
params = {
    "n_neighbors":[1,3,5],
    "weights":["uniform","distance"],
    "metric":["euclidean","manhattan"]
}


# In[20]:


grid = GridSearchCV(
    estimator=model,
    param_grid=params,
    cv=3,
    scoring="accuracy"
)
grid.fit(x_train, y_train)


# In[21]:


x_train.shape


# In[22]:


print(grid.best_params_)


# In[23]:


print(grid.best_score_)


# In[24]:


best_model = grid.best_estimator_

prediction = best_model.predict(x_test)


# In[25]:


prediction


# In[26]:


best_model


# In[ ]:




