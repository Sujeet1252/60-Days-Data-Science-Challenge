#!/usr/bin/env python
# coding: utf-8

# # Feature Scaling

# In[ ]:


import pandas as pd
from sklearn.preprocessing import MinMaxScaler
df=pd.DataFrame({'Age':[20,30,40],'Salary':[25000,50000,75000]})
print(pd.DataFrame(MinMaxScaler().fit_transform(df),columns=df.columns))

