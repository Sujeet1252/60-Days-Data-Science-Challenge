#!/usr/bin/env python
# coding: utf-8

# In[3]:


import matplotlib.pyplot as plt
import numpy as np

for i in range(50):
    print(random.randint(1,200),end=",")


# In[15]:


no = [153,10,197,103,187,77,118,48,36,114,172,82,155,24,195,162,79,171,
       52,73,20,102,137,110,60,28,60,103,160,136,127,76,66,176,
       5,168,123,194,181,113,34,75,182,2,70,165,88,29,181,99]

l = [20,40,60,80,100,120,140,160,180,200]

plt.hist(no,color='y',bins=l,edgecolor="r")

plt.title("Histogram")
plt.xlabel("Python")
plt.ylabel("No")
plt.show()


# In[ ]:




