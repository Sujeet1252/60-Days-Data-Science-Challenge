#!/usr/bin/env python
# coding: utf-8

# # Support Vector Machine Regression
# 
# Linear Dataset

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


dataset = pd.read_csv("placement.csv")
dataset.head()


# In[3]:


dataset.isnull().sum()


# In[4]:


plt.figure(figsize=(4,3))
sns.scatterplot(x="cgpa" , y= "package" , data =dataset)
plt.show()


# In[5]:


x= dataset[["cgpa"]]
y = dataset["package"]


# In[6]:


from sklearn.model_selection import train_test_split
x_train , x_test , y_train , y_test = train_test_split(
    x,
    y,
    random_state = 42,
    test_size = 0.2
)


# In[7]:


from sklearn.svm import SVR


# In[8]:


sv = SVR(kernel = "linear")
sv.fit(x_train,y_train)


# In[9]:


sv.score(x_test,y_test)*100


# In[10]:


sv.score(x_train,y_train)*100


# In[11]:


plt.figure(figsize=(4,3))
sns.scatterplot(x="cgpa" , y= "package" , data =dataset)
plt.plot(dataset["cgpa"],sv.predict(x),color="red")
plt.show()

