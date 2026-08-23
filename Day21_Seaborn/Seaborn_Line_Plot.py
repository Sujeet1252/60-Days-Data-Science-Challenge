#!/usr/bin/env python
# coding: utf-8

# In[8]:


import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

var = [1,2,3,4,5,6,7]
var_1 = [2,3,4,1,5,6,7]

x_1 = pd.DataFrame({"var":var, "var_1":var_1})

sns.lineplot (x = "var", y = "var_1",data = x_1 )

plt.show()


# In[12]:


y_1 = sns.load_dataset("penguins")
y_1


# In[19]:


sns.lineplot (x = "bill_depth_mm", y = "flipper_length_mm",data = y_1,hue= "sex" ,style = "sex", palette = 'Accent', markers = ["o","<"])

plt.show()


# In[20]:


y_1 = sns.load_dataset("penguins").head(20)
y_1


# In[23]:


sns.lineplot (x = "bill_depth_mm", y = "flipper_length_mm",data = y_1)
plt.show()

