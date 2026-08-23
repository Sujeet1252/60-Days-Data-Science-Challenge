#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = sns.load_dataset("titanic")


# In[2]:


df


# In[3]:


df.isnull().sum()


# In[4]:


fare = df["fare"].dropna()

median_fare = fare.median()
print(f"Median of Fare is : {median_fare :.2f}")


# In[5]:


md = df["fare"].median()
print(md)


# In[6]:


sns.histplot(x= "fare",data=df,bins=[i for i in range(0,80,10)])
plt.plot([md for i in range(0,300)], [i for i in range(0,300)],c="red")
plt.show()

