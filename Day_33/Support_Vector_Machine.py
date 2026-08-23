#!/usr/bin/env python
# coding: utf-8

# # Support Vector Machine

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from mlxtend.plotting import plot_decision_regions


# In[2]:


dataset = pd.read_csv("placement (1).csv")
dataset.head()


# In[3]:


dataset.isnull().sum()


# In[4]:


plt.figure(figsize=(5,3))
sns.scatterplot(x="cgpa",y="iq",data=dataset,hue="placement")
plt.show()


# In[5]:


x = dataset[["cgpa","iq"]]

y = dataset["placement"]


# In[6]:


from sklearn.model_selection import train_test_split

x_train , x_test , y_train , y_test = train_test_split(
    x,
    y,
    random_state =32,
    test_size = 0.2
)


# In[21]:


from sklearn.svm import SVC

sv = SVC(kernel="linear")
sv.fit(x_train,y_train)


# In[22]:


sv.score(x_test,y_test)*100


# In[23]:


sv.score(x_train,y_train) * 100


# In[24]:


plot_decision_regions(X = x.to_numpy(),y = y.to_numpy(),clf=sv)
plt.show()


# In[ ]:




