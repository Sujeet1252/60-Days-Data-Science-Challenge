#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = sns.load_dataset("titanic")
age = df["age"].dropna()

mean_age = age.mean()

print(f"Mean age : {mean_age : .2f}")

plt.figure(figsize=(8,5))
sns.histplot(age, bins = 15, color="red",edgecolor= "black")

plt.axvline(mean_age,color="blue",linewidth = 2, linestyle="--",label=f"Mean = {mean_age : .2f}")

plt.title("Distribution of age")

plt.xlabel("Age")
plt.ylabel("Frequency")
plt.legend()
plt.show()


# In[ ]:




