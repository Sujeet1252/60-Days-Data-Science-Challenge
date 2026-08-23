#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Assistant
import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7]

y = [2,2,5,7,3,8,9]

# Removed 'use_line_collection=False' parameter as it's no longer supported
plt.stem(x,y,linefmt = ":", markerfmt = "ro",bottom = 0,basefmt = "g",label = "Matplot")

plt.legend()
plt.show()


# In[ ]:




