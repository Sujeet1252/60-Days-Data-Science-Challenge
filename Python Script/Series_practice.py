#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd

print("Series of marks")
Marks = pd.Series([45,43,42,44,32,47,49])

print(Marks)

print("\nSeries of Names")
Names = pd.Series(["Sujeet","rohit","Aman","Suman","Mayank"])

print(Names)

print("\nAccess First Element of Names :")
print(Names[0])

print("\nAccess last Element Using Index Location")
print(Names.iloc[-1])

print("\nAccess last Element using Values")
print(Names.values[-1])

