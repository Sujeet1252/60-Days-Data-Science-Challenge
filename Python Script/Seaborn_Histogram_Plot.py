#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


data = sns.load_dataset("penguins")
data


# In[12]:


sns.displot(data["bill_length_mm"],kde = True, rug = True,color = "g")
plt.show()

