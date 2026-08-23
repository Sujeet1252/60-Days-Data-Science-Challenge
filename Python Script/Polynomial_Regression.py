#!/usr/bin/env python
# coding: utf-8

# # Polynomial Regression

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


dataset = pd.read_csv("Ice_cream selling data.csv")
dataset.head()


# In[10]:


dataset.describe()


# In[14]:


dataset.corr()


# In[11]:


dataset.info()
dataset.shape


# In[13]:


plt.figure(figsize=(5,3))
sns.scatterplot(x="Temperature (°C)",y="Ice Cream Sales (units)", data=dataset)
plt.show()


# In[15]:


x = dataset[["Temperature (°C)"]]
y = dataset["Ice Cream Sales (units)"]


# In[17]:


from sklearn.preprocessing import PolynomialFeatures
pf = PolynomialFeatures(degree=2)
pf.fit(x)
x = pf.transform(x)


# In[19]:


from sklearn.model_selection import train_test_split


# In[23]:


x_train, x_test , y_train, y_test = train_test_split(
    x,
    y,
    test_size = 0.2,
    random_state=42
)


# In[24]:


from sklearn.linear_model import LinearRegression


# In[26]:


lr = LinearRegression()
lr.fit(x_train,y_train)


# In[27]:


lr.score(x_test,y_test)*100


# In[28]:


pred = lr.predict(x)


# In[29]:


plt.figure(figsize=(5,3))
plt.plot(dataset["Temperature (°C)"],pred,c="red")
sns.scatterplot(x="Temperature (°C)",y="Ice Cream Sales (units)", data=dataset)
plt.show()


# In[ ]:




