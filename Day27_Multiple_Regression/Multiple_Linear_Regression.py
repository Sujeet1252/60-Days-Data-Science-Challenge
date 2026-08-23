#!/usr/bin/env python
# coding: utf-8

# # Multiple Linear Regression

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[4]:


dataset = pd.read_csv("Student_Performance.csv")
dataset.head()


# In[5]:


dataset.describe()


# In[6]:


dataset.isnull().sum()


# In[7]:


dataset.info()


# In[8]:


from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
dataset["Extracurricular Activities"] = le.fit_transform(dataset["Extracurricular Activities"])


# In[12]:


plt.figure(figsize=(5,3))
sns.heatmap(data=dataset.corr(),annot=True)
plt.show()


# In[13]:


x = dataset.iloc[:,:-1]
y = dataset["Performance Index"]


# In[16]:


from sklearn.model_selection import train_test_split


# In[17]:


x_train , x_test , y_train , y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42
)


# In[18]:


from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(x_train,y_train)


# In[19]:


lr.score(x_test,y_test)*100


# In[20]:


lr.coef_


# In[21]:


lr.intercept_


# In[22]:


# y_pred = 2.85248393 * Hours Studies 1.0169882 * Previous Scores + -33.921946215556126


# In[27]:


y_predict = lr.predict(x_test)
y_predict


# In[28]:


print(y_predict[:10])


# In[30]:


comparison = pd.DataFrame({
    "Actual" : y_test,
    "Predicted" : y_predict
})

print(comparison.head(10))


# In[32]:


new_student = pd.DataFrame({
    "Hours Studied": [7],
    "Previous Scores": [80],
    "Extracurricular Activities": [1],
    "Sleep Hours": [8],
    "Sample Question Papers Practiced": [5]
})

prediction = lr.predict(new_student)
print(prediction)


# In[ ]:




