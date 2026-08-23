#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = sns.load_dataset("titanic")
fare = df["fare"].dropna()

median_fare = fare.median()

print(f"Median fare : {median_fare : .2f}")

plt.figure(figsize=(8,5))
sns.histplot(fare, bins = 15, color="red",edgecolor= "black")

plt.axvline(median_fare,color="blue",linewidth = 2, linestyle="--",
            label=f"Median = {median_fare : .2f}")

plt.title("Distribution of fare")

plt.xlabel("fare")
plt.ylabel("Frequency")
plt.legend()
plt.show()


# In[ ]:




