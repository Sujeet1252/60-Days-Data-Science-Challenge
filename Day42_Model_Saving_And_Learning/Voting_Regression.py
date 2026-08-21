#!/usr/bin/env python
# coding: utf-8

# # Voting Regression

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


dataset = pd.read_csv("placement.csv")
dataset.head()


# In[3]:


x = dataset.iloc[:,:-1]
y = dataset["package"]


# In[5]:


from sklearn.model_selection import train_test_split

x_train , x_test , y_train , y_test = train_test_split(
    x,
    y,
    random_state=42,
    test_size=0.2
)


# In[12]:


from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR


# In[ ]:





# In[13]:


lr = LinearRegression()
lr.fit(x_train,y_train)


# In[14]:


lr.score(x_train,y_train)*100 , lr.score(x_test,y_test)*100


# In[15]:


dt = DecisionTreeRegressor()
dt.fit(x_train,y_train)


# In[16]:


dt.score(x_train,y_train)*100 , dt.score(x_test,y_test)*100


# In[17]:


sv = SVR()
sv.fit(x_train,y_train)


# In[18]:


sv.score(x_train,y_train)*100 , sv.score(x_test,y_test)*100


# In[ ]:





# In[ ]:





# In[19]:


from sklearn.ensemble import VotingRegressor


# In[22]:


li = [("lr1",LinearRegression()),("dt1",DecisionTreeRegressor()),("sv1",SVR())]


# In[25]:


vc = VotingRegressor(li)
vc.fit(x_train,y_train)


# In[26]:


vc.score(x_train,y_train)*100 , vc.score(x_test,y_test)*100


# In[28]:


pred = {"dt1":dt.predict(x_test),"sv1":sv.predict(x_test),"lr1":lr.predict(x_test),"vc":vc.predict(x_test)}
pd.DataFrame(pred).head(3)


# In[29]:


(2.9200	+ 2.745462 + 2.780313)/3


# In[ ]:




