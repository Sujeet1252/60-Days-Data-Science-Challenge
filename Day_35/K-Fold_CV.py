#!/usr/bin/env python
# coding: utf-8

#  # K - Fold Crosss Validation

# In[1]:


import pandas as pd

from sklearn.model_selection import (
train_test_split,
cross_val_score,
KFold
)

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier


# In[2]:


data = {
    "Age":[20,22,25,28,30,35,40,45,50,55],
    "Salary":[20000,25000,30000,35000,45000,50000,60000,70000,80000,90000],
    "Purchased":[0,0,0,0,1,1,1,1,1,1]
}

df = pd.DataFrame(data)
df


# In[3]:


X = df[["Age","Salary"]]
y = df["Purchased"]


# In[17]:


# K - Fold Cross Validation


# In[22]:


model = KNeighborsClassifier(n_neighbors=5)
score = cross_val_score(
    model,
    X,
    y,
    cv = 4
)
print(score * 100)


# In[23]:


print(score.mean() * 100)


# In[24]:


# K - Fold Object


# In[33]:


kf = KFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

score = cross_val_score(
    model,
    X,
    y,
    cv = kf
)

print(score * 100)


# In[34]:


print(score.mean() * 100)


# In[35]:


# Stratified K - Fold


# In[36]:


from sklearn.model_selection import StratifiedKFold

skf = StratifiedKFold(
    n_splits= 4, 
    shuffle= True,
    random_state= 42
)

score = cross_val_score(
    model,
    X,
    y,
    cv = skf
)
print(score * 100)


# In[37]:


print(score.mean() * 100)

