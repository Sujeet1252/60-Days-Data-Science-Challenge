#!/usr/bin/env python
# coding: utf-8

# In[13]:


import numpy as np

marks = np.array([15,41,78,96,23,56,41,63])

print("=" * 35)
print("       STUDENT MARKS ANALYSIS")
print("=" * 35)

print("\nMarks:")
print(marks)

print("\n----- RANGE -----")
print(f"Range (Max - Min) : {np.max(marks) - np.min(marks)}")

print("\n----- STUDENTS ABOVE 80 -----")
above_80 = marks[marks > 80]
print(f"Count : {len(above_80)}")
print(f"Marks : {above_80}")

print("\n----- STUDENTS BELOW 60 -----")
below_60 = marks[marks < 60]
print(f"Count : {len(below_60)}")
print(f"Marks : {below_60}")

print("\n----- HIGHEST SCORER -----")
print(f"Highest Marks : {np.max(marks)}")

print("\n----- LOWEST SCORER -----")
print(f"Lowest Marks : {np.min(marks)}")

print("\n----- SORTED MARKS -----")
print(np.sort(marks))

