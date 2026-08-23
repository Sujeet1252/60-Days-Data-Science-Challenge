#!/usr/bin/env python
# coding: utf-8

# # SVM Regression
# 
# Polynomial Dataset

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


data = pd.read_csv("Ice_cream selling data.csv")
data.head()


# In[3]:


plt.figure(figsize=(4,3))
sns.scatterplot(x="Temperature (°C)" , y= "Ice Cream Sales (units)" , data =data)
plt.show()


# In[4]:


x = data[["Temperature (°C)"]]
y = data["Ice Cream Sales (units)"]


# In[5]:


from sklearn.model_selection import train_test_split
x_train ,x_test, y_train , y_test = train_test_split(
    x,
    y,
    random_state=42,
    test_size = 0.2
) 


# In[6]:


from sklearn.svm import SVR


# In[25]:


sv = SVR()
sv.fit(x_train,y_train)


# In[26]:


sv.score(x_test,y_test)*100


# In[27]:


sv.score(x_train,y_train)*100


# In[28]:


plt.figure(figsize=(4,3))
sns.scatterplot(x="Temperature (°C)" , y= "Ice Cream Sales (units)" , data =data)
plt.plot(data["Temperature (°C)"],sv.predict(x),color="red")
plt.show()

