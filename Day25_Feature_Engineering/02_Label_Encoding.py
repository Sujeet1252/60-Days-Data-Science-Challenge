#!/usr/bin/env python
# coding: utf-8

# # Label Encoding

# In[ ]:


import pandas as pd
from sklearn.preprocessing import LabelEncoder
df=pd.DataFrame({'Gender':['Male','Female','Male']})
le=LabelEncoder()
df['Gender_Encoded']=le.fit_transform(df['Gender'])
print(df)

