#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = sns.load_dataset("penguins")
data


# In[6]:


sns.scatterplot(x="bill_depth_mm",y="flipper_length_mm",data=data,hue="sex")
plt.show()


# In[9]:


data = sns.load_dataset("penguins").head(20)

sns.scatterplot(x="bill_depth_mm",y="flipper_length_mm",data=data,hue="sex",style = "sex",size="sex",sizes =(100,60))
plt.show()


# In[13]:


data = sns.load_dataset("penguins").head(20)

sns.scatterplot(x="bill_depth_mm",y="flipper_length_mm",data=data,hue="sex",style = "sex",size="sex",sizes =(100,60),palette = 'gist_ncar')
plt.show()


# In[ ]:




