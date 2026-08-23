#!/usr/bin/env python
# coding: utf-8

# In[10]:


import scipy.stats as st
import numpy as np


# In[11]:


x = 90
u = 82
std = 20
n = 81
ap = 0.05


# In[12]:


z_calc  = (x-u)/(std/np.sqrt(n))
z_calc


# In[14]:


z_table = st.norm.ppf(1-ap)
z_table


# In[16]:


if z_table < z_calc :
    print(" Ha is right")
else :
    print(" Ha is not")


# In[ ]:




