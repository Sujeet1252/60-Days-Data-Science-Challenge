#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


# In[7]:


dataset = sns.load_dataset("titanic")
dataset.head(10)


# In[10]:


dataset["age"].skew()


# In[8]:


#Left Skewness
sns.histplot(x="age",data=dataset)
plt.show()


# In[11]:


data = np.random.normal(0,100,100)


# In[12]:


df = pd.DataFrame({"x":data})
df["x"].skew()


# In[13]:


#Right Skewness

sns.histplot(x="x",data=df)
plt.show()


# In[19]:


data =  [2,3,3,4,4,4,5,5,5,5,6,6,6,6,6,7,7,7,7,7,7,8,8,8,8,8,9,9,9,9,10,10,10,11,11,12]
df = pd.DataFrame({"x":data})
df["x"].skew()


# In[22]:


#No Skewness

sns.histplot(x="x",data=df,bins = [2,3,4,5,6,7,8,9,10,11,12,13])
plt.show()


# In[ ]:




