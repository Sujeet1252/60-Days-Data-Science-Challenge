#!/usr/bin/env python
# coding: utf-8

# # Naive Baye's 

# In[1]:


import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from mlxtend.plotting import plot_decision_regions


# In[2]:


dataset = pd.read_csv("placement (1).csv")
dataset.head()


# In[5]:


plt.figure(figsize=(5,3))
sns.scatterplot(x="cgpa",y="iq",data=dataset, hue="placement")
plt.show()


# In[7]:


sns.kdeplot(data=dataset["iq"])
plt.show()


# In[18]:


x = dataset[["cgpa","iq"]]
y = dataset["placement"]


# In[19]:


from sklearn.model_selection import train_test_split 

x_train , x_test , y_train , y_test = train_test_split(
    x,
    y,
    random_state=42,
    test_size=0.2
) 


# In[20]:


from sklearn.naive_bayes import GaussianNB , MultinomialNB , BernoulliNB


# In[21]:


gnb = GaussianNB()
gnb.fit(x_train,y_train)


# In[25]:


gnb.score(x_test, y_test)*100 , gnb.score(x_train, y_train)*100


# In[26]:


mnb = MultinomialNB()
mnb.fit(x_train , y_train)


# In[27]:


mnb.score(x_test, y_test)*100 , mnb.score(x_train, y_train)*100


# In[28]:


bnb = BernoulliNB()
bnb.fit(x_train , y_train)


# In[29]:


bnb.score(x_test, y_test)*100 , bnb.score(x_train, y_train)*100


# In[33]:


plt.figure(figsize=(5,3))
plot_decision_regions(x.to_numpy(), y.to_numpy(),clf=gnb)
plt.show()


# In[34]:


plt.figure(figsize=(5,3))
plot_decision_regions(x.to_numpy(), y.to_numpy(),clf=mnb)
plt.show()


# In[35]:


plt.figure(figsize=(5,3))
plot_decision_regions(x.to_numpy(), y.to_numpy(),clf=bnb)
plt.show()


# In[ ]:




