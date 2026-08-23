#!/usr/bin/env python
# coding: utf-8

# # Regularization

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


dataset =pd.read_csv("Housing.csv")
dataset.head()


# In[3]:


dataset.describe()


# In[4]:


plt.figure(figsize=(8,5))
sns.heatmap(data = dataset.corr(numeric_only=True),annot=True)
plt.show()


# In[5]:


from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

categorical_columns = [
    "mainroad",
    "guestroom",
    "basement",
    "hotwaterheating",
    "airconditioning",
    "prefarea",
    "furnishingstatus"
]

for col in categorical_columns:
    dataset[col] = le.fit_transform(dataset[col])


# In[8]:


X = dataset.drop("price",axis=1)
y = dataset["price"]


# In[9]:


from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# In[10]:


from sklearn.linear_model import Ridge

ridge = Ridge(alpha=1.0)
ridge.fit(X_train, y_train)
print("Ridge Score:", ridge.score(X_test, y_test))


# In[11]:


from sklearn.linear_model import Lasso

lasso = Lasso(alpha=1.0)
lasso.fit(X_train, y_train)
print("Lasso Score:", lasso.score(X_test, y_test))


# In[12]:


print("Ridge Coefficients")
print(ridge.coef_)

print("Lasso Coefficients")
print(lasso.coef_)


# In[ ]:




