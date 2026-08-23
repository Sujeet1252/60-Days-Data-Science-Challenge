#!/usr/bin/env python
# coding: utf-8

# # Customer Purchase Prediction System

# In[1]:


import pandas as pd

data = {
    "Age":[20,22,25,28,30,35,40,45,50,55],
    "Income":[20000,25000,30000,35000,45000,50000,60000,70000,80000,90000],
    "SpendingScore":[20,25,30,40,45,60,65,70,75,85],
    "Purchased":[0,0,0,0,1,1,1,1,1,1]
}

df = pd.DataFrame(data)


# In[5]:


print("Dataset Inspection")

print("Shpae is " , df.shape )
print("=="*15)
df.info()
print("=="*15)
df.describe()


# In[7]:


x = df[["Age","Income","SpendingScore"]]

y = df["Purchased"]


# In[8]:


from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier


# In[9]:


x_train , x_test , y_train , y_test = train_test_split(
    x,
    y,
    random_state = 42 , 
    test_size = 0.2
)


# In[10]:


scaler = StandardScaler()

x_train = scaler.fit_transform(x_train)

x_test = scaler.transform(x_test)


# In[11]:


knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(x_train,y_train)


# In[16]:


prediction = knn.predict(x_test)

print(prediction)


# In[19]:


new_customer = scaler.transform([[29,42000,50]])

print(knn.predict(new_customer))


# In[20]:


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


# In[21]:


from sklearn.metrics import accuracy_score

k_values = [1, 3, 5, 7]
accuracy = []

for k in k_values:
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(x_train, y_train)

    prediction = model.predict(x_test)

    acc = accuracy_score(y_test, prediction) * 100
    accuracy.append(acc)

    print(f"K = {k} --> Accuracy = {acc:.2f}%")


# In[22]:


best_k = k_values[accuracy.index(max(accuracy))]
print("Best K =", best_k)
print("Best Accuracy =", max(accuracy))


# In[24]:


import matplotlib.pyplot as plt

plt.figure(figsize=(5,3))
plt.plot(k_values, accuracy, marker="o", linewidth=2)
plt.title("Accuracy vs K Value")
plt.xlabel("K Value")
plt.ylabel("Accuracy (%)")
plt.grid(True)
plt.show()


# In[25]:


from sklearn.metrics import confusion_matrix
import seaborn as sns

best_model = KNeighborsClassifier(n_neighbors=best_k)
best_model.fit(x_train, y_train)

prediction = best_model.predict(x_test)

cm = confusion_matrix(y_test, prediction)

plt.figure(figsize=(5,4))
sns.heatmap(cm,
            annot=True,
            fmt="d",
            cmap="Blues",
            xticklabels=["Not Purchased","Purchased"],
            yticklabels=["Not Purchased","Purchased"])

plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()


# In[26]:


comparison = pd.DataFrame({
    "Actual": y_test.values,
    "Predicted": prediction
})

print(comparison.head(10))


# In[27]:


comparison.head(10).plot(kind="bar", figsize=(7,3))
plt.title("Actual vs Predicted")
plt.xlabel("Customer")
plt.ylabel("Purchased")
plt.show()


# In[ ]:




