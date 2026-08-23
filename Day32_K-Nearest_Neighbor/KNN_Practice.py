#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier


# In[3]:


data = {
    "Age":[20,22,25,28,30,35,40,45,50,55],
    "Salary":[20000,25000,30000,35000,45000,50000,60000,70000,80000,90000],
    "Purchased":[0,0,0,0,1,1,1,1,1,1]
}

df = pd.DataFrame(data)
df


# In[4]:


X = df[["Age","Salary"]]

y = df["Purchased"]


# In[5]:


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# In[11]:


scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)

X_test = scaler.transform(X_test)


# In[12]:


model = KNeighborsClassifier(
    n_neighbors=3
)

model.fit(X_train, y_train)


# In[13]:


prediction = model.predict(X_test)

print(prediction)


# In[14]:


new_customer = scaler.transform([[32,48000]])

print(model.predict(new_customer))


# In[17]:


from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

print("Accuracy:", accuracy_score(y_test, prediction))
print("--"*10)
print(confusion_matrix(y_test, prediction))
print("--"*10)
print(classification_report(y_test, prediction))


# In[ ]:




