#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# In[2]:


data = {
    "Area": [1000,1200,1500,1800,2000,2200,2500,3000],
    "Bedrooms": [2,2,3,3,4,4,4,5],
    "Age": [10,8,7,6,5,4,3,2],
    "Price": [35,40,50,60,70,75,85,100]
}
df = pd.DataFrame(data)


# In[3]:


print("Shape is :",df.shape)
print(df.info())
print(df.describe())


# In[4]:


X = df[["Area","Bedrooms","Age"]]
y = df["Price"]


# In[5]:


X_train,X_test,y_train,y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)


# In[6]:


model = LinearRegression()
model.fit(X_train,y_train)


# In[7]:


y_pred = model.predict(X_test)


# In[8]:


mae = mean_absolute_error(y_test,y_pred)
print(mae)


# In[9]:


mse = mean_squared_error(y_test,y_pred)
print(mse)


# In[10]:


rmse = np.sqrt(mse)
print(rmse)


# In[11]:


r2 = r2_score(y_test,y_pred)
print(r2)


# In[12]:


plt.figure(figsize=(8,5))
sns.scatterplot(
    x="Area",
    y="Price",
    data=df,
    s=100
)
plt.show()


# In[13]:


plt.figure(figsize=(8,5))
sns.regplot(
    x="Area",
    y="Price",
    data=df
)
plt.show()


# In[14]:


comparison = pd.DataFrame({
    "Actual":y_test.values,
    "Predicted":y_pred
})
comparison.plot(
    kind="bar",
    figsize=(8,5)
)
plt.title("Actual vs Predicted")
plt.show()


# In[15]:


print("Business Questions\n")
print("\nWhich house is the most expensive?")
print(df.loc[df["Price"].idxmax()])
print("\nDoes area affect price?")
print(df[["Area","Price"]].corr())
print("\nDoes age affect price?")
print(df[["Age","Price"]].corr())
print("\n Predicted New House Price")
new_house = pd.DataFrame({
    "Area":[2100],
    "Bedrooms":[4],
    "Age":[4]
})

prediction = model.predict(new_house)

print("Predicted Price =", prediction[0])


# In[ ]:




