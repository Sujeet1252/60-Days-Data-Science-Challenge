#!/usr/bin/env python
# coding: utf-8

# # Binning

# In[ ]:


import pandas as pd
df=pd.DataFrame({'Age':[18,22,35,45]})
df['Age_Group']=pd.cut(df['Age'],bins=[0,25,40,100],labels=['Young','Adult','Senior'])
print(df)

