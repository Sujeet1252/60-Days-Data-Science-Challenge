#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = sns.load_dataset("titanic")
data.head(10)


# In[2]:


print(data["age"].mean())


# In[3]:


mn = np.mean(data["age"])


# In[4]:


sns.histplot(x= "age",data=data,bins=[i for i in range(0,80,10)])
plt.plot([mn for i in range(0,300)], [i for i in range(0,300)],c="red")
plt.show()

