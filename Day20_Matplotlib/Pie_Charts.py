#!/usr/bin/env python
# coding: utf-8

# In[27]:


import matplotlib.pyplot as plt

labels = ["A", "B", "C","D"]
sizes = [30, 25, 25, 20]
ex=[0.2,0.0,0.0,0.0]
c = ['r','g','y','b']

plt.pie(sizes, labels=labels, autopct="%1.1f%%",explode=ex,colors=c,shadow =True,radius=.7,startangle=0,textprops={"fontsize":15})
plt.title("Share Distribution")
plt.legend()
plt.show()


# In[ ]:




