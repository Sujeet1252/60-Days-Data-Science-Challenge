#!/usr/bin/env python
# coding: utf-8

# # Regression Analysis
# Simple Linear Regression

# In[25]:


import pandas as pd  
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score


# In[26]:


dataset = pd.read_csv(r"Salary_dataset.csv")
dataset.head()


# In[27]:


print(dataset.info())


# In[28]:


print(dataset.isnull().sum())


# In[29]:


if "Unnamed: 0" in dataset.columns:
    dataset.drop("Unnamed: 0", axis=1,inplace=True)


# In[30]:


print(dataset.describe())


# In[31]:


plt.figure(figsize=(5,3))
sns.scatterplot(x="YearsExperience",
                y="Salary",
                data= dataset)
plt.title("Years Of Experience vs Salary")
plt.show()


# In[41]:


x = dataset[["YearsExperience"]]
y = dataset["Salary"]


# In[42]:


x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42
)


# In[44]:


model = LinearRegression()
model.fit(x_train,y_train)


# In[45]:


print("Slope (Coffecient):",model.coef_[0])
print("Intercept:",model.intercept_)


# In[46]:


y_pred = model.predict(x_test)


# In[47]:


print("\n Model Performance")
print("R Square score :",r2_score(y_test,y_pred))
print("MAE  :", mean_absolute_error(y_test,y_pred))
print("MSE  :", mean_squared_error(y_test,y_pred))
print("RMSE  :", mean_squared_error(y_test,y_pred)**0.5)


# In[49]:


new_data = pd.DataFrame({"YearsExperience":[2.3]})
prediction = model.predict(new_data)
print("\n Predicted Salary for 2.3 years Experience = {:.2f}".format(prediction[0]))


# In[52]:


plt.figure(figsize=(5,3))
sns.scatterplot(x="YearsExperience",
                y="Salary",
                data= dataset,
                color="blue"
)

plt.plot(
    dataset["YearsExperience"],
    model.predict(x),
    color="red",
    linewidth=2
)
plt.title("Simple Linear Regression")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()


# In[54]:


print("\nRegression Equation")
print(f"Salary = {model.intercept_:.2f}+({model.coef_[0]:.2f} * YearsExperience)")


# In[ ]:




