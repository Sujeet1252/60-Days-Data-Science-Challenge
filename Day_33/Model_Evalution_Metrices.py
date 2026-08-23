#!/usr/bin/env python
# coding: utf-8

# # Model Evaluation Metrices

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


df = pd.read_csv("customer_purchase_dataset.csv")
df.head()


# In[4]:


df.shape


# In[27]:


X = df[["Age","Income","CreditScore","PreviousPurchases"]]
y = df["Purchased"]


# In[28]:


from sklearn.model_selection import train_test_split
X_train , X_test , y_train , y_test = train_test_split(
    X,
    y,
    random_state = 42,
    test_size = 0.2
)


# In[29]:


from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train, y_train)


# In[30]:


y_pred = model.predict(X_test)


# In[31]:


from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)


# In[32]:


from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test, y_pred)
print(accuracy)


# In[33]:


from sklearn.metrics import precision_score
precision = precision_score(y_test, y_pred)
print(precision)


# In[34]:


from sklearn.metrics import recall_score
recall = recall_score(y_test, y_pred)
print(recall)


# In[35]:


from sklearn.metrics import f1_score
f1 = f1_score(y_test, y_pred)
print(f1)


# In[36]:


from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))


# In[37]:


from sklearn.metrics import roc_auc_score
prob = model.predict_proba(X_test)[:,1]
auc = roc_auc_score(y_test, prob)
print(auc)


# In[39]:


plt.figure(figsize=(3,2))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()


# In[41]:


plt.figure(figsize=(5,3))
from sklearn.metrics import roc_curve
fpr, tpr, _ = roc_curve(y_test, prob)
plt.plot(fpr, tpr, label="Logistic Regression")
plt.plot([0,1],[0,1],'--')
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.legend()
plt.show()


# In[43]:


plt.figure(figsize=(5,3))
plt.bar(["Accuracy","F1 Score"], [accuracy, f1])
plt.show()


# In[ ]:




