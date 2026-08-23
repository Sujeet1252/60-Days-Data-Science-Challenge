#!/usr/bin/env python
# coding: utf-8

# # DBSCAN Clustering Algorithm

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import make_moons


# In[2]:


x , y = make_moons(n_samples=250,noise=0.05)


# In[12]:


df = {"data1":x[:,0], "data2":x[:,1]}


# In[13]:


dataset = pd.DataFrame(df)
dataset.head(3)


# In[15]:


plt.figure(figsize=(4,3))
sns.scatterplot(x="data1",y="data2",data=dataset)
plt.show()


# In[17]:


from sklearn.cluster import DBSCAN
db = DBSCAN(
    eps=0.2,
    min_samples=5,
    metric='euclidean'
)
dataset["Predict"] = db.fit_predict(dataset)


# In[18]:


plt.figure(figsize=(4,3))
sns.scatterplot(x="data1",y="data2",data=dataset,hue ="Predict")
plt.show()


# In[ ]:




