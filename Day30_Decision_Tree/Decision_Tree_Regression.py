#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


dataset = pd.read_csv("multiple_linear_regression_dataset.csv")
dataset.head(3)


# In[14]:


dataset.shape


# In[19]:


plt.figure(figsize=(1,1))
sns.pairplot(data = dataset)
plt.show()


# In[21]:


x = dataset[["age", "experience"]]
y = dataset["income"]


# In[22]:


from sklearn.model_selection import train_test_split

x_train , x_test , y_train , y_test = train_test_split(
    x,
    y,
    random_state = 42,
    test_size = 0.2
)


# In[26]:


from sklearn.tree import DecisionTreeRegressor , plot_tree

dt = DecisionTreeRegressor(
    max_depth=4,
    min_samples_split=3,
    min_samples_leaf=2,
    random_state=42
)
dt.fit(x_train,y_train)


# In[27]:


dt.score(x_test,y_test)*100 , dt.score(x_train,y_train)*100


# In[28]:


plot_tree(dt)
plt.show()


# In[29]:


from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

prediction = dt.predict(x_test)

print("MAE :", mean_absolute_error(y_test, prediction))
print("MSE :", mean_squared_error(y_test, prediction))
print("RMSE:", mean_squared_error(y_test, prediction) ** 0.5)
print("R2 :", r2_score(y_test, prediction))


# In[ ]:




