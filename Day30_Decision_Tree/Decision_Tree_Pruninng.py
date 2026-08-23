#!/usr/bin/env python
# coding: utf-8

# # Decision Tree Pruning

# # Pre - Pruning

# In[1]:


import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


dataset = pd.read_csv("Social_Network_Ads.csv")
dataset.head()


# In[3]:


x = dataset[["Age","EstimatedSalary"]]
y = dataset["Purchased"]


# In[4]:


from sklearn.preprocessing import StandardScaler

sc = StandardScaler()

sc.fit(x)

x = pd.DataFrame(sc.transform(x),columns=x.columns)


# In[5]:


from sklearn.model_selection import train_test_split

x_train , x_test , y_train , y_test = train_test_split(
    x,
    y,
    random_state= 42,
    test_size= 0.2
)


# In[6]:


from sklearn.tree import DecisionTreeClassifier

dt = DecisionTreeClassifier(max_depth=3)

dt.fit(x_train,y_train)


# In[7]:


dt.score(x_test,y_test)*100


# In[8]:


dt.score(x_train,y_train)*100


# In[9]:


from mlxtend.plotting import plot_decision_regions
plot_decision_regions(x.to_numpy(),y.to_numpy(),clf=dt)
plt.show()


# In[10]:


dt.predict([[19,76000]])


# In[11]:


from sklearn.tree import plot_tree
plt.figure(figsize=(20,20))
plot_tree(dt)
plt.savefig("tree.jpg")
plt.show()


# In[ ]:





# # Post - Pruning

# In[12]:


for i in range(1,20):
    dt2 = DecisionTreeClassifier(max_depth=i)
    dt2.fit(x_train,y_train)
    print(dt2.score(x_train,y_train),dt2.score(x_test,y_test),i)


# In[ ]:




