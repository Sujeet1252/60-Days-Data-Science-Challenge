#!/usr/bin/env python
# coding: utf-8

# # Feature Creation

# In[ ]:


import pandas as pd
df=pd.DataFrame({'Price':[500,700,900],'Quantity':[2,3,5]})
df['Revenue']=df['Price']*df['Quantity']
print(df)

