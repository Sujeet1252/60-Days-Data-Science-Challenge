#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data = {
    "Age":[20,22,25,28,30,35,40,45,50,55],
    "Salary":[20000,25000,30000,35000,45000,50000,60000,70000,80000,90000],
    "Purchased":[0,0,0,0,1,1,1,1,1,1]
}

df = pd.DataFrame(data)
df


# In[3]:


x = df[["Age","Salary"]]
y = df["Purchased"]


# In[7]:


from sklearn.model_selection import train_test_split
x_train , x_test , y_train , y_test = train_test_split(
    x,
    y,
    random_state=42,
    test_size=0.2,
    stratify=y
)


# In[11]:


from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)
print(x_train)


# In[10]:


from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(
    n_neighbors=5,
    weights='uniform',
    algorithm='auto'
)
knn.fit(x_train,y_train)


# In[12]:


prediction = knn.predict(x_test)

print("Prediction :", prediction)
print("Actual",y_test.values)


# In[17]:


from sklearn.model_selection import cross_val_score

scores = cross_val_score(
    KNeighborsClassifier(n_neighbors=3),
    x,
    y,
    cv=4
)

print(scores)


# In[19]:


print("Mean Accuracy :",scores.mean() * 100)


# In[20]:


from sklearn.model_selection import KFold

kf = KFold(
    n_splits=4,
    shuffle=True,
    random_state=42
)

scores = cross_val_score(
    KNeighborsClassifier(3),
    x,
    y,
    cv=kf
)

print(scores)
print(scores.mean()*100)


# In[22]:


from sklearn.model_selection import StratifiedKFold

skf = StratifiedKFold(
    n_splits=4,
    shuffle=True,
    random_state=42
)

scores = cross_val_score(
    KNeighborsClassifier(3),
    x,
    y,
    cv=skf
)

print(scores)
print(scores.mean()*100)


# In[26]:


from sklearn.metrics import accuracy_score

model = KNeighborsClassifier(3)

model.fit(x_train,y_train)

pred = model.predict(x_test)

test_accuracy = accuracy_score(y_test,pred) * 100

cv_accuracy = cross_val_score(
    KNeighborsClassifier(3),
    x,
    y,
    cv=4
).mean() * 100

print("Train Test Accuracy :",test_accuracy)

print("Cross Validation Accuracy :",cv_accuracy)


# In[27]:


from sklearn.pipeline import Pipeline
pipe = Pipeline([
    ("scaler",StandardScaler()),
    ("knn",KNeighborsClassifier())
])
pipe.fit(x_train,y_train)
pred = pipe.predict(x_test)
print(pred)


# In[28]:


from sklearn.pipeline import make_pipeline
pipe = make_pipeline(
    StandardScaler(),
    KNeighborsClassifier()
)
pipe.fit(x_train,y_train)
pred = pipe.predict(x_test)
print(pred)


# In[29]:


from sklearn.pipeline import Pipeline
pipe = Pipeline([
    ("scaler",StandardScaler()),
    ("knn",KNeighborsClassifier(n_neighbors=3))
])
pipe.fit(x_train,y_train)
print(pipe.predict(x_test))


# In[30]:


from sklearn.linear_model import LogisticRegression
pipe = Pipeline([
    ("scaler",StandardScaler()),
    ("lr",LogisticRegression())
])
pipe.fit(x_train,y_train)
prediction = pipe.predict(x_test)
print(prediction)


# In[32]:


from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV

pipe = Pipeline([
    ("scaler",StandardScaler()),
    ("knn",KNeighborsClassifier())
])

params = {
    "knn__n_neighbors":[1,3,5,7],
    "knn__weights":["uniform","distance"],
    "knn__metric":["euclidean","manhattan"]
}

grid = GridSearchCV(
    pipe,
    params,
    cv=4,
    scoring="accuracy"
)

grid.fit(x,y)

print("Best Parameters")
print(grid.best_params_)

print()

print("Best Accuracy")
print(grid.best_score_ * 100)


# In[ ]:




