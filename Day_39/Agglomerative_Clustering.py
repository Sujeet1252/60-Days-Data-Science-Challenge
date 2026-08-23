#!/usr/bin/env python
# coding: utf-8

# # Hierarchical Clustering

# # AGGLOMERATIVE CLUSTERING

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


data = sns.load_dataset("iris")
X = data.drop("species",axis=1)
X.head(3)


# In[3]:


plt.figure(figsize=(4,2))
sns.pairplot(data=X)
plt.show()


# In[4]:


import scipy.cluster.hierarchy as sc
plt.figure(figsize=(20,20))

sc.dendrogram(
    sc.linkage(X, method='ward', metric='euclidean')
)

plt.savefig("Clustering.jpg")

plt.show()


# In[5]:


from sklearn.cluster import AgglomerativeClustering
ac = AgglomerativeClustering(n_clusters=2,linkage='ward')
X["Predict"] = ac.fit_predict(X)


# In[6]:


X.head(3)


# In[7]:


plt.figure(figsize=(4,2))
sns.pairplot(data=X,hue="Predict")
plt.show()


# In[ ]:





# In[ ]:




