#!/usr/bin/env python
# coding: utf-8

# # Logistic Regression

# In[1]:


import pandas as pd

data = {
    "Hours":[1,2,3,4,5,6,7,8,9,10],
    "Attendance":[60,65,70,75,80,85,90,95,96,98],
    "Pass":[0,0,0,0,1,1,1,1,1,1]
}

df = pd.DataFrame(data)


# In[4]:


df


# In[5]:


X = df[["Hours", "Attendance"]]
y = df["Pass"]


# In[6]:


from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# In[7]:


from sklearn.linear_model import LogisticRegression

model = LogisticRegression()

model.fit(X_train, y_train)


# In[8]:


prediction = model.predict(X_test)

print(prediction)


# In[9]:


model.predict_proba(X_test)


# In[12]:


from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, prediction)*100

print("Accuracy:", accuracy)


# In[11]:


from sklearn.metrics import confusion_matrix

print(confusion_matrix(y_test, prediction))


# In[ ]:




