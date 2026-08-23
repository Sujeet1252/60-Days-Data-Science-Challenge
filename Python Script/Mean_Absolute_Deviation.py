#!/usr/bin/env python
# coding: utf-8

# In[1]:


import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load dataset
df = sns.load_dataset("tips")

# Select column
x = df["total_bill"]

# Calculate statistics
mean = x.mean()
mad = np.mean(np.abs(x - mean))

# Plot
plt.figure(figsize=(8,5))

sns.histplot(x, bins=15, color="skyblue", edgecolor="black")

# Mean line
plt.axvline(mean,
            color="red",
            linestyle="--",
            linewidth=2,
            label=f"Mean = {mean:.2f}")

# Mean - MAD
plt.axvline(mean-mad,
            color="green",
            linestyle=":",
            linewidth=2,
            label=f"Mean - MAD = {mean-mad:.2f}")

# Mean + MAD
plt.axvline(mean+mad,
            color="green",
            linestyle=":",
            linewidth=2,
            label=f"Mean + MAD = {mean+mad:.2f}")

plt.title("Mean Absolute Deviation of Total Bill")
plt.xlabel("Total Bill ($)")
plt.ylabel("Frequency")
plt.legend()
plt.grid(alpha=0.3)

plt.show()

print(f"Mean = {mean:.2f}")
print(f"Mean Absolute Deviation = {mad:.2f}")


# In[ ]:




