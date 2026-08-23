#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd

data = {
    "Age":[21,22,23,24,25],
    "Salary":[25000,20000,15000,40000,55000],
    "Experience":[1,2,3,4,5]
}

df = pd.DataFrame(data)


# In[8]:


print(df)


# In[9]:


df.corr()


# In[10]:


import matplotlib.pyplot as plt

df["Salary"].hist()

plt.show()


# In[11]:


import seaborn as sns

sns.boxplot(x=df["Salary"])


# In[14]:


sns.heatmap(df.corr(), annot=True)


# In[ ]:




