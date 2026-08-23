#!/usr/bin/env python
# coding: utf-8

# # Loan Approval Model Optimization

# In[1]:


import pandas as pd
data = pd.read_csv("loan_approval_dataset.csv")
data.head(3)


# In[2]:


print(" ====== Dataset Inspection ======= ")
print("\n Shape of Dataset")
print(data.shape)

print("\n Dataset Columns Name : ")
print(data.columns)

print("\n Dataset Information :")
data.info()

print("\n Check Missing Values ")
print(data.isnull().sum())


# In[3]:


from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
data[" education"] = le.fit_transform(data[" education"])
data[" self_employed"] = le.fit_transform(data[" self_employed"])
data[" loan_status"] = le.fit_transform(data[" loan_status"])


# In[4]:


X = data.drop([" loan_id"," loan_status"],axis = 1 , errors="ignore")
y = data[" loan_status"]


# In[5]:


X.head()


# In[6]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# In[7]:


from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train  =  scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


# In[8]:


from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier()
model.fit(X_train, y_train)


# In[9]:


model.score(X_train , y_train ) *100  , model.score(X_test , y_test ) *100 


# In[10]:


y_pred = model.predict(X_test)


# In[11]:


from sklearn.metrics import (
accuracy_score, precision_score, recall_score, f1_score
)
accuracy = accuracy_score(y_test,y_pred) * 100
precision = precision_score(y_test,y_pred) * 100
recall = recall_score(y_test,y_pred) * 100
f1 = f1_score(y_test,y_pred) * 100

print("Accuracy :",accuracy)
print("Precision:",precision)
print("Recall :",recall)
print("F1 Score :",f1)


# In[12]:


from sklearn.model_selection import GridSearchCV
params = {
    "n_neighbors":[3,5,7,9,11],
    "weights":["uniform","distance"],
    "metric":["euclidean","manhattan"]
}


# In[13]:


grid = GridSearchCV(
    estimator=KNeighborsClassifier(),
    param_grid=params,
    cv=5,
    scoring="accuracy",
    n_jobs=-1
)
grid.fit(X_train,y_train)


# In[14]:


print(grid.best_params_)


# In[15]:


print(grid.best_score_ * 100)


# In[16]:


best_model = grid.best_estimator_
print(best_model)

grid_pred = best_model.predict(X_test)
print(grid_pred)

grid_accuracy = accuracy_score(y_test,grid_pred) * 100
print(grid_accuracy)


# In[17]:


from sklearn.model_selection import RandomizedSearchCV
random = RandomizedSearchCV(
    estimator=KNeighborsClassifier(),
    param_distributions=params,
    n_iter=10,
    cv=5,
    scoring="accuracy",
    random_state=42,
    n_jobs=-1
)
random.fit(X_train,y_train)


# In[18]:


print(random.best_params_)


# In[20]:


random_model = random.best_estimator_
print(best_model)

random_pred = random_model.predict(X_test)
print(random_pred)

random_accuracy = accuracy_score(y_test , random_pred) * 100
print(random_accuracy)


# In[21]:


import pandas as pd

comparison = pd.DataFrame({
    "Model":[
        "Default KNN",
        "GridSearchCV",
        "RandomizedSearchCV"
    ],
    "Accuracy":[
        accuracy,
        grid_accuracy,
        random_accuracy
    ]
})

comparison


# In[22]:


import matplotlib.pyplot as plt

plt.figure(figsize=(6,4))

plt.bar(comparison["Model"],comparison["Accuracy"])

plt.title("Model Accuracy Comparison")
plt.ylabel("Accuracy")

plt.show()


# In[ ]:




