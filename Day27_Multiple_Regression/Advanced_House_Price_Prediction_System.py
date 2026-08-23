#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


data = {
    "Area":[1000,1200,1500,1800,2000,2200,2500,3000],
    "Bedrooms":[2,2,3,3,4,4,4,5],
    "Bathrooms":[1,2,2,2,3,3,3,4],
    "Age":[10,8,7,6,5,4,3,2],
    "Parking":[1,1,2,2,2,3,3,4],
    "Price":[35,40,50,60,70,75,85,100]
}

df = pd.DataFrame(data)


# In[3]:


df.head()
df.shape
df.columns
df.info()
df.describe()
df.isnull().sum()
df.duplicated().sum()


# In[5]:


sns.pairplot(df)
plt.show()


# In[6]:


sns.heatmap(df.corr(),annot=True)
plt.show()


# In[7]:


sns.boxplot(df["Price"])
plt.show()


# In[8]:


X = df.drop("Price",axis=1)

y = df["Price"]


# In[9]:


from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test=train_test_split(
X,
y,
test_size=0.2,
random_state=42
)


# In[10]:


from sklearn.linear_model import LinearRegression

model=LinearRegression()

model.fit(X_train,y_train)


# In[12]:


model.score(X_test,y_test)*100


# In[13]:


prediction=model.predict(X_test)


# In[14]:


from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

mae=mean_absolute_error(y_test,prediction)

mse=mean_squared_error(y_test,prediction)

rmse=np.sqrt(mse)

r2=r2_score(y_test,prediction)


# In[15]:


coef=pd.DataFrame({
"Feature":X.columns,
"Coefficient":model.coef_
})

coef


# In[16]:


comparison=pd.DataFrame({
"Actual":y_test,
"Predicted":prediction
}).reset_index(drop=True)

comparison.head(10)


# In[17]:


new_house=pd.DataFrame({

"Area":[2300],
"Bedrooms":[4],
"Bathrooms":[3],
"Age":[4],
"Parking":[2]

})

model.predict(new_house)


# In[18]:


plt.scatter(df["Area"],df["Price"])
plt.xlabel("Area")
plt.ylabel("Price")
plt.show()


# In[19]:


coef.plot(
x="Feature",
y="Coefficient",
kind="bar"
)
plt.show()


# In[20]:


plt.scatter(y_test,prediction)

plt.xlabel("Actual")

plt.ylabel("Predicted")

plt.show()


# In[ ]:




