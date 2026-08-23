#!/usr/bin/env python
# coding: utf-8

# # Date Features

# In[ ]:


import pandas as pd
df=pd.DataFrame({'Date':['2022-01-10','2023-05-20']})
df['Date']=pd.to_datetime(df['Date'])
df['Year']=df['Date'].dt.year
print(df)

