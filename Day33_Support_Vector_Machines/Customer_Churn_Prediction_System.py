#!/usr/bin/env python
# coding: utf-8

# # Customer Churn Prediction System

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


data = {
    "Tenure":[2,5,8,12,15,20,24,30,36,48],
    "MonthlyCharges":[70,65,80,55,50,45,40,35,30,25],
    "SupportCalls":[5,4,4,3,2,2,1,1,0,0],
    "Churn":[1,1,1,1,0,0,0,0,0,0]
}

df = pd.DataFrame(data)
df


# In[11]:


print("===== Dataset Inspection  =====")
print(df.columns)
print(df.shape)
print(df.describe())
print(df.info())


# In[13]:


x = df[["Tenure","MonthlyCharges","SupportCalls"]]
y = df["Churn"]


# In[16]:


from sklearn.model_selection import train_test_split
x_train , x_test , y_train , y_test = train_test_split(
    x,
    y,
    random_state = 42 , 
    test_size = 0.2
)


# In[22]:


from sklearn.svm import SVC
model = SVC(kernel="linear",probability=True,random_state=42)
model.fit(x_train,y_train)


# In[23]:


model.score(x_train,y_train)*100


# In[24]:


model.score(x_test,y_test)*100


# In[61]:


new = [[15,50,12]]
prediction = model.predict(new)
if prediction[0] == 1:
    print("Customer will churn")
else:
    print("Customer will stay")


# In[55]:


from sklearn.metrics import accuracy_score
y_pred = model.predict(x_test)
accuracy = accuracy_score(y_test,y_pred)*100

print("Accuracy :", accuracy)


# In[56]:


from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test,y_pred)
print(cm)


# In[57]:


from sklearn.metrics import classification_report
print(classification_report(y_test,y_pred))


# In[58]:


probability = model.predict_proba(new)*100
print(probability)


# In[59]:


plt.figure(figsize=(5,3))
sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=["Stay","Churn"],
    yticklabels=["Stay","Churn"]
)
plt.xlabel("Prediction")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()


# In[60]:


comparison = pd.DataFrame(
    {
        "Actual" : y_test.values,
        "Predicted" : y_pred
    }
)
comparison.plot(kind="bar",figsize=(4,2))
plt.title("Actual Vs Predicted")
plt.show()


# In[47]:


df[["Tenure","MonthlyCharges","SupportCalls"]].hist(figsize=(6,4))
plt.tight_layout()
plt.show()


# In[ ]:




