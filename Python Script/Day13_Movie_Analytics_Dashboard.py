#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

movies = {
    "Movie": [
        "Jawan",
        "Pathaan",
        "KGF 2",
        "Dangal",
        "RRR",
        "3 Idiots",
        "Animal"
    ],

    "Genre": [
        "Action",
        "Action",
        "Action",
        "Drama",
        "Action",
        "Comedy",
        "Drama"
    ],

    "Rating": [
        8.1,
        7.8,
        8.5,
        8.4,
        8.2,
        8.4,
        7.9
    ],

    "Revenue": [
        1150,
        1050,
        1250,
        2000,
        1350,
        450,
        900
    ]
}

df = pd.DataFrame(movies)

print("=" * 50)
print("       MOVIE ANALYTICS DASHBOARD")
print("=" * 50)

print("\nMovie Dataset")
print(df)

# Basic Statistics
print("\n===== BASIC ANALYSIS =====")

print("Total Movies        :", len(df))

print("Average Rating      :",
      round(df["Rating"].mean(), 2))

print("Highest Rating      :",
      df["Rating"].max())

print("Lowest Rating       :",
      df["Rating"].min())

print("Highest Revenue     :",
      df["Revenue"].max())

print("Lowest Revenue      :",
      df["Revenue"].min())

# Highest Rated Movie
top_movie = df.loc[df["Rating"].idxmax()]

print("\nHighest Rated Movie")
print(top_movie)

# Highest Revenue Movie
revenue_movie = df.loc[df["Revenue"].idxmax()]

print("\nHighest Revenue Movie")
print(revenue_movie)

# Top 3 Movies
print("\n===== TOP 3 MOVIES =====")

top3 = df.sort_values(
    by="Rating",
    ascending=False
).head(3)

print(top3)

# Genre Analysis
print("\n===== GENRE ANALYSIS =====")

genre_rating = df.groupby("Genre")["Rating"].mean()

print("\nAverage Rating by Genre")
print(genre_rating)

genre_revenue = df.groupby("Genre")["Revenue"].sum()

print("\nRevenue by Genre")
print(genre_revenue)

print("\nMost Profitable Genre")

print(genre_revenue.idxmax())

print("=" * 50)

