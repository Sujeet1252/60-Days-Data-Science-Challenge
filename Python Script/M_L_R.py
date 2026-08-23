#!/usr/bin/env python
# coding: utf-8

# In[1]:


# ===============================
# 1. Import Libraries
# ===============================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ===============================
# 2. Load Dataset
# ===============================

dataset = pd.read_csv("Student_Performance.csv")

print(dataset.head())

# ===============================
# 3. Dataset Information
# ===============================

print(dataset.shape)
print(dataset.info())
print(dataset.describe())
print(dataset.isnull().sum())

# ===============================
# 4. Encode Categorical Column
# ===============================

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

dataset["Extracurricular Activities"] = le.fit_transform(
    dataset["Extracurricular Activities"]
)

# Yes = 1
# No = 0

# ===============================
# 5. Correlation Heatmap
# ===============================

plt.figure(figsize=(7,5))

sns.heatmap(
    dataset.corr(),
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Matrix")
plt.show()

# ===============================
# 6. Separate Features & Target
# ===============================

X = dataset.drop("Performance Index", axis=1)

y = dataset["Performance Index"]

# ===============================
# 7. Train Test Split
# ===============================

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# ===============================
# 8. Train Model
# ===============================

from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(X_train, y_train)

# ===============================
# 9. Model Parameters
# ===============================

print("Intercept")
print(model.intercept_)

print()

print("Coefficients")
print(model.coef_)

coef = pd.DataFrame({
    "Feature":X.columns,
    "Coefficient":model.coef_
})

print(coef)

# ===============================
# 10. Model Accuracy
# ===============================

accuracy = model.score(X_test,y_test)

print("R² Score =",accuracy)

# ===============================
# 11. Predict Test Data
# ===============================

y_pred = model.predict(X_test)

# ===============================
# 12. Compare Actual vs Predicted
# ===============================

comparison = pd.DataFrame({
    "Actual":y_test,
    "Predicted":y_pred
}).reset_index(drop=True)

print(comparison.head(10))

# ===============================
# 13. Evaluation Metrics
# ===============================

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

mae = mean_absolute_error(y_test,y_pred)

mse = mean_squared_error(y_test,y_pred)

rmse = np.sqrt(mse)

r2 = r2_score(y_test,y_pred)

print("MAE :",mae)
print("MSE :",mse)
print("RMSE :",rmse)
print("R² :",r2)

# ===============================
# 14. Predict New Student
# ===============================

new_student = pd.DataFrame({

    "Hours Studied":[7],
    "Previous Scores":[80],
    "Extracurricular Activities":[1],
    "Sleep Hours":[8],
    "Sample Question Papers Practiced":[5]

})

prediction = model.predict(new_student)

print("Predicted Performance =",prediction[0])


# In[ ]:




