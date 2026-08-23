#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas  as pd


# In[3]:


dataset = pd.read_csv("loan.csv")
dataset.head()


# In[8]:


dataset.shape


# In[4]:


x = dataset[["income","credit_score"]]
y= dataset["loan_status"]


# In[14]:


from sklearn.model_selection import train_test_split

x_train, x_test , y_train, y_test = train_test_split(
    x,
    y,
    random_state = 42,
    test_size=0.2
)


# In[15]:


from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier(random_state=42)


# In[16]:


model.fit(x_train, y_train)


# In[18]:


prediction = model.predict(x_test)

print(prediction)


# In[20]:


from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, prediction) * 100

print(accuracy)


# In[21]:


from sklearn.metrics import confusion_matrix

print(confusion_matrix(y_test , prediction))


# In[22]:


from sklearn.tree import plot_tree
import matplotlib.pyplot as plt


# In[26]:


plt.figure(figsize = (5,3))
plot_tree(
    model,
    filled  = True,
    feature_names= x.columns,
    class_names=model.classes_
)
plt.show()


# In[ ]:




