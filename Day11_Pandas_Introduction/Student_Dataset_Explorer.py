#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd

students = {
    "Name": ["Sujeet", "Rahul", "Aman", "Priya", "Neha"],
    "Marks": [90, 85, 78, 92, 88],
    "Age": [23, 22, 21, 22, 23],
    "City": ["Varanasi", "Delhi", "Lucknow", "Kanpur", "Patna"]
}

df = pd.DataFrame(students)

print("===== STUDENT DATASET =====")
print(df)

print("\nTotal Students:", len(df))

print("Average Marks:", df["Marks"].mean())

print("Highest Marks:", df["Marks"].max())

print("Lowest Marks:", df["Marks"].min())

topper = df.loc[df["Marks"].idxmax()]

print("\n===== TOPPER =====")
print(topper)

def grade(mark):
    if mark >= 90:
        return "A+"
    elif mark >= 80:
        return "A"
    elif mark >= 70:
        return "B"
    else:
        return "C"

print("\n=== Student Grade ===")
df["Grade"] = df["Marks"].apply(grade)

print(df)

