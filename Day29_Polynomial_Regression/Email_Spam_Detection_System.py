#!/usr/bin/env python
# coding: utf-8

# # Email Spam Detection System

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


data = {
    "Free":[1,1,0,0,1,0,1,0],
    "Offer":[1,1,0,0,1,0,0,0],
    "Money":[1,0,0,0,1,0,1,0],
    "Urgent":[1,1,0,0,0,0,1,0],
    "Spam":[1,1,0,0,1,0,1,0]
}

df = pd.DataFrame(data)
df


# In[4]:


X = df[["Free","Offer","Money","Urgent"]]
y = df["Spam"]


# In[5]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# In[6]:


from sklearn.naive_bayes import GaussianNB

model = GaussianNB()

model.fit(X_train, y_train)


# In[8]:


new_email = pd.DataFrame(
    [[1,1,0,1]],
    columns=["Free","Offer","Money","Urgent"]
)
prediction = model.predict(new_email)

if prediction[0] == 1:
    print("Spam Email")
else:
    print("not Spam")


# In[10]:


probability = model.predict_proba(new_email) * 100
print(probability)


# In[12]:


from sklearn.metrics import accuracy_score

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred) * 100

print("Accuracy :", accuracy)


# In[13]:


from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, y_pred)

print(cm)


# In[14]:


from sklearn.metrics import classification_report

print(classification_report(y_test, y_pred))


# In[15]:


from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=3)

knn.fit(X_train, y_train)

knn_accuracy = knn.score(X_test, y_test) * 100

nb_accuracy = model.score(X_test, y_test) * 100

print("Gaussian Naive Bayes Accuracy :", nb_accuracy)

print("KNN Accuracy :", knn_accuracy)


# In[16]:


if nb_accuracy > knn_accuracy:
    print("Gaussian Naive Bayes performs better.")
elif knn_accuracy > nb_accuracy:
    print("KNN performs better.")
else:
    print("Both models perform equally.")


# In[17]:


import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(5,3))

sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=["Not Spam","Spam"],
    yticklabels=["Not Spam","Spam"]
)

plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()


# In[18]:


comparison = pd.DataFrame({
    "Actual": y_test.values,
    "Predicted": y_pred
})

comparison.plot(kind="bar", figsize=(5,3))

plt.title("Actual vs Predicted")

plt.show()


# In[20]:


feature_count = X.sum()

feature_count.plot(
    kind="bar",
    figsize=(6,4),
    color=["blue","green","orange","red"]
)

plt.title("Feature Frequency")

plt.xlabel("Features")

plt.ylabel("Count")

plt.show()


# In[ ]:




