#!/usr/bin/env python
# coding: utf-8

# # K - Nearest Neighbor (Regression)

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from mlxtend.plotting import plot_decision_regions


# In[3]:


dataset = pd.read_csv("Salary_Data.csv")
dataset.head(3)


# In[4]:


dataset.shape


# In[5]:


dataset.isnull().sum()


# In[7]:


dataset["Age"] = dataset["Age"].fillna(dataset["Age"].mean())

dataset["Years of Experience"] = dataset["Years of Experience"].fillna(dataset["Years of Experience"].mean())

dataset["Salary"] = dataset["Salary"].fillna(dataset["Salary"].mean())


# In[8]:


data = dataset[["Age","Years of Experience","Salary"]]


# In[9]:


data.head()


# In[10]:


data.isnull().sum()


# In[11]:


x = data[["Age", "Years of Experience"]]

y = data["Salary"]


# In[12]:


from sklearn.model_selection import train_test_split

x_train , x_test , y_train , y_test = train_test_split(
    x,
    y,
    random_state=42,
    test_size=0.2
)


# In[23]:


from sklearn.neighbors import KNeighborsRegressor

knn = KNeighborsRegressor(n_neighbors=8)

knn.fit(x_train , y_train)


# In[24]:


knn.score(x_test , y_test) *100


# In[ ]:




