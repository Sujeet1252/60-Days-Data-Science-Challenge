#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

marks = np.array([54,45,65,62,53,51,65])

print("=" * 40)
print("      STUDENT MARKS ANALYSIS")
print("=" * 40)

print("\nMarks:")
print(marks)

print("\n----- BASIC STATISTICS -----")

print(f"Mean        : {np.mean(marks):.2f}")
print(f"Meadian     : {np.median(marks):2f}")
print(f"Minimum Marks    : {np.min(marks)}")
print(f"Maximum Marks   : {np.max(marks)}")

print("\n----- DISPERSION MEASURES -----")

print(f"Variance   : {np.var(marks)}")
print(f"Standard Variarnce   : {np.std(marks)}")

print("\n----- PERCENTILES -----")

print(f"25th Percentile   : {np.percentile(marks, 25)}")
print(f"50th Percentile   : {np.percentile(marks, 50)}")
print(f"75th Percentile   : {np.percentile(marks, 75)}")



