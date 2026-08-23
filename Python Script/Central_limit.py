#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[5]:


data = [np.random.randint(10,100) for i in range(1000)]
table = pd.DataFrame({"data": data})
table


# In[7]:


plt.figure(figsize = (3,2))
sns.kdeplot(x="data",data = table)
plt.show()


# In[ ]:




