#!/usr/bin/env python
# coding: utf-8

# In[5]:


import matplotlib.pyplot as plt

x = [2,3,4,5,6,7]
y= [3,4,3,1,2,4]

plt.scatter(x,y,color='r')
plt.title("Charts")
plt.xlabel("DAY")
plt.ylabel("NO.")
plt.show()


# In[16]:


import matplotlib.pyplot as plt

x = [2,3,4,5,6,7]
y= [3,4,3,1,2,4]

colors=['r','g','y','b','r','g']
sizes = [250,200,180,120,300,350]
plt.scatter(x,y,c=colors,s=sizes,marker="*",edgecolor='b')
plt.title("Charts")
plt.xlabel("DAY")
plt.ylabel("NO.")
plt.show()


# In[18]:


import matplotlib.pyplot as plt

x = [2,3,4,5,6,7]
y= [3,4,3,1,2,4]

colors=[20,3,25,13,15,20]
sizes = [250,200,180,120,300,350]


plt.scatter(x,y,c=colors,s=sizes,cmap="viridis")
plt.colorbar()
plt.title("Charts")
plt.xlabel("DAY")
plt.ylabel("NO.")
plt.show()


# In[21]:


import matplotlib.pyplot as plt

x = [2,3,4,5,6,7]
y= [3,4,3,1,2,4]
z= [8,7,2,6,9,5]

colors=[20,3,25,13,15,20]
sizes = [250,200,180,120,300,350]


plt.scatter(x,y,c=colors,s=sizes,cmap="viridis")
plt.scatter(x,z,color='r',s=sizes)


plt.colorbar()
plt.title("Charts")
plt.xlabel("DAY")
plt.ylabel("NO.")
plt.show()


# In[ ]:




