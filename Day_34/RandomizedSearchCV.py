#!/usr/bin/env python
# coding: utf-8

# # RandomizedSearchCV

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


from sklearn.model_selection import (
    train_test_split,
    RandomizedSearchCV
)

from sklearn.neighbors import KNeighborsClassifier


# In[4]:


data = {
    "Age":[20,22,25,28,30,35,40,45,50,55],
    "Salary":[20000,25000,30000,35000,45000,50000,60000,70000,80000,90000],
    "Purchased":[0,0,0,0,1,1,1,1,1,1]
}

df = pd.DataFrame(data)
df.head()


# In[5]:


X = df[["Age","Salary"]]

y = df["Purchased"]


# In[6]:


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# In[7]:


model = KNeighborsClassifier()


# In[8]:


params = {
    "n_neighbors":[3,5,7,9],
    "weights":["uniform","distance"],
    "metric":["euclidean","manhattan"]
}


# In[9]:


random = RandomizedSearchCV(
    KNeighborsClassifier(),
    estimator=model,
    param_distributions=params,
    n_iter=5,
    cv=5,
    random_state=42
)

random.fit(X_train, y_train)


# In[ ]:




