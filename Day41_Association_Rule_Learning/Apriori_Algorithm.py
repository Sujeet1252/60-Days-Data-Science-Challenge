#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[11]:


data = pd.read_csv("groceries - groceries.csv")
data.head(3)


# In[12]:


data.shape


# In[13]:


data.columns


# In[14]:


market = []
for i in range(0,data.shape[0]):
    cust = []
    for j in data.columns :
        if type(data[j][i])==str:
            cust.append(data[j][i])

    market.append(cust)


# In[16]:


l = []
for i in market:
    for j in i :
        l.append(j)


# In[20]:


import collections
p = collections.Counter(l)


# In[23]:


d = {"Item Name":p.keys(),"values":p.values()}
pd.DataFrame(d).sort_values(by=["values"],ascending=False)


# In[27]:


from mlxtend.preprocessing.transactionencoder import TransactionEncoder
tr = TransactionEncoder()
tr.fit(market)


# In[30]:


df = pd.DataFrame(tr.transform(market),columns=tr.columns_)
df


# In[33]:


from mlxtend.frequent_patterns import apriori
ap = apriori(df,min_support=0.05,use_colnames=True,max_len=3)
ap.sort_values(by=["support"])


# In[ ]:




