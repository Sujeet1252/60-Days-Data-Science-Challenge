#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

data = {
    "Hours":[1,2,3,4,5,6,7,8,9,10],
    "Attendance":[60,65,70,75,80,85,90,95,96,98],
    "Assignments":[40,45,55,60,70,75,80,85,90,95],
    "Pass":[0,0,0,0,1,1,1,1,1,1]
}

df = pd.DataFrame(data)


# In[2]:


df


# In[3]:


df.shape
df.info()
df.describe()


# In[4]:


X = df[["Hours", "Attendance", "Assignments"]]
y = df["Pass"]


# In[5]:


from sklearn.model_selection import train_test_split

X_train , X_test , y_train , y_test = train_test_split(
    X,
    y,
    random_state= 42,
    test_size = 0.2
)


# In[6]:


from sklearn.linear_model import LogisticRegression

model = LogisticRegression()

model.fit(X_train , y_train)


# In[7]:


prediction = model.predict(X_test)

print(prediction)


# In[11]:


new_student = pd.DataFrame({
    "Hours":[6],
    "Attendance":[82],
    "Assignments":[78]
})

result = model.predict(new_student)

if result[0] == 1:
    print("Student Will Pass")
else:
    print("Student Will Fail")


# In[15]:


probability = model.predict_proba(new_student)

print(f"Fail Probability : {probability[0][0]*100:.2f}%")
print(f"Pass Probability : {probability[0][1]*100:.2f}%")


# In[16]:


from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, prediction)

print("Accuracy:", accuracy)


# In[20]:


from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, prediction)

print(cm)


# In[21]:


from sklearn.metrics import classification_report

print(classification_report(y_test, prediction))


# In[23]:


import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(4,3))

sns.heatmap(
    cm,
    annot=True,
    cmap="Blues",
    fmt="d"
)

plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")

plt.show()


# In[24]:


comparison = pd.DataFrame({
    "Actual": y_test.values,
    "Predicted": prediction
})

comparison.plot(kind="bar", figsize=(6,4))

plt.title("Actual vs Predicted")

plt.show()


# In[25]:


coef = pd.DataFrame({
    "Feature":X.columns,
    "Coefficient":model.coef_[0]
})

print(coef)


# In[26]:


print(model.intercept_)


# In[ ]:




