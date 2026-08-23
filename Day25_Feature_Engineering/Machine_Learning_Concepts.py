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


# Load Dataset
dataset = pd.read_csv("Salary_dataset.csv")
dataset.head()


# In[5]:


# Separate Features & Target
x = dataset[["YearsExperience"]]
y = dataset["Salary"]


# In[6]:


# Train-Test Split
x_train , x_test , y_train , y_test = train_test_split(
    x,
    y,
    test_size = 0.2,
    random_state=42
)


# In[7]:


# Create Linear Regression Model
model = LinearRegression()


# In[8]:


# Train Model
model.fit(x_train,y_train)


# In[9]:


#Predict Test Values
y_pred = model.predict(x_test)


# In[12]:


# Display Prediction
prediction = pd.DataFrame({
    "Actual Salary" : y_test,
    "Predicted Salary" : y_pred
})
print(prediction)


# In[19]:


# Predict New Salary
new_employee = pd.DataFrame({
    "YearsExperience":[2.3]
})

salary = model.predict(new_employee)

print("Predicted Salary =", salary[0])


# In[20]:


# CAlculate MEan Absolute Error
mae = mean_absolute_error(y_test,y_pred)
print("MAE =",mae)


# In[21]:


# Calculate Mean Squared Error
mse = mean_squared_error(y_test, y_pred)

print("MSE =", mse)


# In[22]:


# calculate RMSE
rmse = np.sqrt(mse)
print("RMSE = ",rmse)


# In[23]:


# CAlculate R2 Score
r2 = r2_score(y_test,y_pred)
print("R2 Score = ", r2)


# In[25]:


# Plot regresssion Line
plt.figure(figsize=(8,5))

plt.scatter(x_train, y_train, color="blue")

plt.plot(
    x_train,
    model.predict(x_train),
    color="red"
)

plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.title("Simple Linear Regression")

plt.show()


# In[26]:


# Model Coefficient
print("Coefficient =", model.coef_[0])


# In[27]:


# Model Intercept
print("Intercept =", model.intercept_)


# In[28]:


# Regression Equation
print("\nRegression Equation")

print(
    f"Salary = {model.intercept_:.2f} + ({model.coef_[0]:.2f} × YearsExperience)"
)


# In[29]:


# Residual Analysis
residuals = y_test - y_pred

residual_df = pd.DataFrame({
    "Actual": y_test,
    "Predicted": y_pred,
    "Residual": residuals
})

print(residual_df)


# In[30]:


#PLot Residuals
plt.figure(figsize=(7,4))

plt.scatter(y_pred, residuals)

plt.axhline(y=0, color="red")

plt.xlabel("Predicted Salary")
plt.ylabel("Residual")

plt.title("Residual Plot")

plt.show()


# In[31]:


# Predict Multiple New Employees
new_data = pd.DataFrame({
    "YearsExperience":[1,3,5,7,10]
})

prediction = model.predict(new_data)

result = new_data.copy()

result["Predicted Salary"] = prediction

print(result)


# In[ ]:




