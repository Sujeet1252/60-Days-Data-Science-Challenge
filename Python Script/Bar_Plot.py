#!/usr/bin/env python
# coding: utf-8

# In[12]:


import matplotlib.pyplot as plt

x = ["python" , "c", "c++" , "java" ]

y =  [85,60,70,82]

plt.xlabel("Languages", fontsize = 15)

plt.ylabel("Popularity", fontsize = 15)

c= ["g","r","y","b" ]

plt.bar(x,y,color = c,width=0.5, align = "center",edgecolor = "r",linewidth=5,linestyle=":",alpha=0.7,label="Ranking")
plt.legend()

plt.show()


# In[24]:


import matplotlib.pyplot as plt
import numpy as np

x = ["python" , "c", "c++" , "java" ]
y =  [85,60,70,82]
z = [10,20,30,40]

width =0.2
p = np.arange(len(x))
p1= [j+width for j in p]

plt.xlabel("Languages", fontsize = 15)
plt.ylabel("Popularity", fontsize = 15)
plt.title("Visualization",fontsize = 15)


plt.bar(p,y,width,color = "r",label="2026")
plt.bar(p1,z,width,color = "b",label="2025")
plt.xticks(p,x)
plt.legend()

plt.show()


# In[25]:


import matplotlib.pyplot as plt
import numpy as np

x = ["python" , "c", "c++" , "java" ]
y =  [85,60,70,82]
z = [10,20,30,40]

width =0.2
p = np.arange(len(x))
p1= [j+width for j in p]

plt.xlabel("Languages", fontsize = 15)
plt.ylabel("Popularity", fontsize = 15)
plt.title("Visualization",fontsize = 15)


plt.barh(p,y,width,color = "r",label="2026")
plt.barh(p1,z,width,color = "b",label="2025")
plt.xticks(p,x)
plt.legend()

plt.show()


# In[ ]:




