#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = sns.load_dataset("titanic")
fare = df["fare"].dropna()

mode_fare = fare.mode()[0]

print(f"Mode of fare : {mode_fare}")

plt.figure(figsize=(8,5))
sns.histplot(fare, bins = 15, color="red",edgecolor= "black")

plt.axvline(mode_fare,color="blue",linewidth = 2,
            label=f"Mode = {mode_fare}")

plt.title("Distribution of fare")

plt.xlabel("fare")
plt.ylabel("Frequency")
plt.legend()
plt.show()


# In[ ]:




