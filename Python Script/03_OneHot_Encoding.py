#!/usr/bin/env python
# coding: utf-8

# # One Hot Encoding

# In[ ]:


import pandas as pd
df=pd.DataFrame({'City':['Delhi','Mumbai','Delhi']})
print(pd.get_dummies(df,columns=['City']))

