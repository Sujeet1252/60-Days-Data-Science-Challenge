#!/usr/bin/env python
# coding: utf-8

# # Disease Prediction Evaluation Dashboard

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df = pd.read_csv("healthcare_disease_prediction_2000.csv")
df.head()


# In[3]:


df.isnull().sum()


# In[4]:


df.columns


# In[5]:


df.shape


# In[6]:


X = df[["Age","BMI", "Blood_Pressure_Systolic",
       "Blood_Pressure_Diastolic", "Cholesterol", "Glucose_Level", "Smoking",
       "Alcohol_Intake", "Physical_Activity", "Family_History"]]

y = df["Heart_Disease"]


# In[7]:


from sklearn.model_selection import train_test_split
X_train , X_test , y_train , y_test = train_test_split(
    X,
    y,
    random_state = 42,
    test_size = 0.2
)


# In[8]:


from sklearn.linear_model import LogisticRegression
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)


# In[9]:


y_pred = model.predict(X_test)


# In[10]:


from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, y_pred)*100

print("Accuracy:", accuracy)


# In[11]:


from sklearn.metrics import precision_score

precision = precision_score(y_test, y_pred)*100

print("Precision:", precision)


# In[12]:


from sklearn.metrics import recall_score

recall = recall_score(y_test, y_pred)*100

print("Recall:", recall)


# In[13]:


from sklearn.metrics import f1_score

f1 = f1_score(y_test, y_pred)*100

print("F1 Score:", f1)


# In[14]:


from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, y_pred)

print(cm)


# In[15]:


from sklearn.metrics import classification_report

print(classification_report(y_test, y_pred))


# In[16]:


from sklearn.metrics import roc_auc_score

y_prob = model.predict_proba(X_test)[:,1]

roc = roc_auc_score(y_test, y_prob)*100

print("ROC-AUC:", roc)


# In[17]:


plt.figure(figsize=(4,3))
sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=["No Disease","Disease"],
    yticklabels=["No Disease","Disease"]
)

plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()


# In[18]:


from sklearn.metrics import roc_curve

fpr, tpr, thresholds = roc_curve(y_test, y_prob)

plt.figure(figsize=(4,3))

plt.plot(fpr, tpr, label="ROC Curve")
plt.plot([0,1],[0,1],'r--')

plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.legend()

plt.show()


# In[19]:


comparison = pd.DataFrame({
    "Actual": y_test.values,
    "Predicted": y_pred
})

comparison.head(20)


# In[20]:


comparison.head(20).plot(kind="bar", figsize=(4,3))

plt.title("Actual vs Predicted")
plt.show()


# In[21]:


importance = pd.DataFrame({
    "Feature": X.columns,
    "Coefficient": model.coef_[0]
})

importance = importance.sort_values(
    by="Coefficient",
    ascending=False
)

print(importance)

