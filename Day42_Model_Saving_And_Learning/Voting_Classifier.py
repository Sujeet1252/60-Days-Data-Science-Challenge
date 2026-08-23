#!/usr/bin/env python
# coding: utf-8

# # Voting Classifiers

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import make_moons


# In[21]:


x , y = make_moons(
    n_samples=1000,
    noise=0.2
)


# In[22]:


df = {"x1":x[:,0],"x2":x[:,1],"y":y}
dataset = pd.DataFrame(df)
dataset


# In[24]:


plt.figure(figsize=(8,4))
sns.scatterplot(x="x1",y="x2",data=dataset,hue="y")
plt.show()


# In[25]:


x_a = dataset.iloc[:,:-1]
y_a = dataset["y"]


# In[26]:


from sklearn.model_selection import train_test_split

x_train , x_test , y_train , y_test = train_test_split(
    x_a,
    y_a,
    random_state=42,
    test_size=0.2
)


# In[27]:


from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB


# In[31]:


dt = DecisionTreeClassifier()
dt.fit(x_train,y_train)


# In[32]:


dt.score(x_train,y_train)*100 , dt.score(x_test,y_test)*100


# In[33]:


sv = SVC()
sv.fit(x_train,y_train)


# In[35]:


sv.score(x_train,y_train)*100 , sv.score(x_test,y_test)*100


# In[36]:


gb = GaussianNB()
gb.fit(x_train,y_train)


# In[37]:


gb.score(x_train,y_train)*100 , gb.score(x_test,y_test)*100


# In[ ]:





# In[ ]:





# In[39]:


from sklearn.ensemble import VotingClassifier


# In[40]:


li = [("dt1",DecisionTreeClassifier()),("sv1",SVC()),("gb1",GaussianNB())]


# In[43]:


vc = VotingClassifier(li,weights=[10,4,7])
vc.fit(x_train,y_train)


# In[44]:


vc.score(x_train,y_train)*100 , vc.score(x_test,y_test)*100


# In[ ]:





# In[ ]:





# In[45]:


pred = {"dt":dt.predict(x_test),"svm":sv.predict(x_test),"gb":gb.predict(x_test),"vc":vc.predict(x_test)}
pd.DataFrame(pred)


# In[ ]:





# In[ ]:




