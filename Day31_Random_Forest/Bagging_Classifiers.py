#!/usr/bin/env python
# coding: utf-8

# # Bagging Classifiers

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import make_moons


# In[2]:


x , y = make_moons(
    n_samples=1000,
    noise=0.2
)


# In[3]:


df = {"x1":x[:,0],"x2":x[:,1],"y":y}
dataset = pd.DataFrame(df)
dataset


# In[4]:


plt.figure(figsize=(8,4))
sns.scatterplot(x="x1",y="x2",data=dataset,hue="y")
plt.show()


# In[5]:


x_a = dataset.iloc[:,:-1]
y_a = dataset["y"]


# In[10]:


from sklearn.model_selection import train_test_split

x_train , x_test , y_train , y_test = train_test_split(
    x_a,
    y_a,
    random_state=43,
    test_size=0.2
)


# In[ ]:





# In[ ]:





# In[11]:


from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC


# In[15]:


bg = BaggingClassifier(estimator=SVC(),n_estimators=50)
bg.fit(x_train,y_train)


# In[16]:


bg.score(x_train,y_train)*100 , bg.score(x_test,y_test)*100


# In[ ]:





# In[ ]:





# In[19]:


rf = RandomForestClassifier(n_estimators=10)
rf.fit(x_train , y_train)


# In[20]:


rf.score(x_train,y_train)*100 , rf.score(x_test,y_test)*100


# In[ ]:




