#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

employees = {
    "Emp_Name": ["  Sujeet  ", "Rahul", "AMAN", "priya"],
    "Salary": [45000.0, 55000.0, 60000.0, 50000.0],
    "Department": ["IT", "HR", "IT", "Finance"]
}

df = pd.DataFrame(employees)

print(df)


# In[2]:


df.rename(columns={"Emp_Name":"Name"}, inplace=True)

print(df)


# In[3]:


print(df.dtypes)

df["Salary"] = df["Salary"].astype(str)

print(df.dtypes)


# In[4]:


df["Salary"] = df["Salary"].astype(float)

df["Salary"] = df["Salary"].astype(int)

print(df)


# In[5]:


df["Department"] = df["Department"].replace({
    "IT":"Technology",
    "HR":"Human Resource"
})

print(df)


# In[6]:


df["Name"] = df["Name"].str.strip()
df["Name"] = df["Name"].str.title()

print(df)


# In[ ]:




