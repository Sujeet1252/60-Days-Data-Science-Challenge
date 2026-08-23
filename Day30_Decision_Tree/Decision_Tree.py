#!/usr/bin/env python
# coding: utf-8

# # Decision Tree

# In[4]:


import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns


# In[5]:


dataset = pd.read_csv("Social_Network_Ads.csv")
dataset.head()


# In[6]:


x = dataset[["Age","EstimatedSalary"]]
y = dataset["Purchased"]


# In[8]:


from sklearn.preprocessing import StandardScaler

sc = StandardScaler()

sc.fit(x)

x = pd.DataFrame(sc.transform(x),columns=x.columns)


# In[9]:


from sklearn.model_selection import train_test_split

x_train , x_test , y_train , y_test = train_test_split(
    x,
    y,
    random_state= 42,
    test_size= 0.2
)


# In[10]:


from sklearn.tree import DecisionTreeClassifier

dt = DecisionTreeClassifier()

dt.fit(x_train,y_train)


# In[11]:


dt.score(x_test,y_test)*100


# In[12]:


dt.predict([[19,76000]])


# In[14]:


from sklearn.tree import plot_tree
plt.figure(figsize=(20,20))
plot_tree(dt)
plt.savefig("tree.jpg")
plt.show()


# In[ ]:




