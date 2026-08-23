#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = sns.load_dataset("tips")
df


# In[2]:


mean = df["total_bill"].mean()

mad = (df["total_bill"] - mean).abs().mean() 

print(" Mean  = ", mean)

print("Mean Absolute Deviation = ",mad)


# In[ ]:




