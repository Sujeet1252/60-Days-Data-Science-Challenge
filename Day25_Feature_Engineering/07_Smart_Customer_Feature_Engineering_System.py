#!/usr/bin/env python
# coding: utf-8

# # Smart Customer Feature Engineering System

# In[ ]:


import pandas as pd
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import seaborn as sns

data={'Customer':['Aman','Rahul','Priya','Neha','Rohit'],'Gender':['Male','Male','Female','Female','Male'],'City':['Delhi','Mumbai','Delhi','Lucknow','Mumbai'],'Age':[22,35,28,41,30],'Salary':[25000,50000,42000,65000,38000],'Purchase':[1500,2200,1800,3500,2700],'Joining_Date':['2022-01-10','2021-06-15','2023-03-20','2020-11-01','2022-09-05']}
df=pd.DataFrame(data)
df['Purchase_Ratio']=df['Purchase']/df['Salary']
df['Salary_per_Age']=df['Salary']/df['Age']
le=LabelEncoder(); df['Gender']=le.fit_transform(df['Gender'])
df=pd.get_dummies(df,columns=['City'])
print(df.head())

