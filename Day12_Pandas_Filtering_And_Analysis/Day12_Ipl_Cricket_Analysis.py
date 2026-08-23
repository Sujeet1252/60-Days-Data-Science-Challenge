#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

data = {
    "Player": ["Virat Kohli", "Rohit Sharma", "MS Dhoni", "KL Rahul", "Shubman Gill"],
    "Runs": [741, 635, 670, 680, 580],
    "Matches": [15, 14, 14, 15, 17],
    "Team": ["RCB", "MI", "CSK", "LSG", "GT"]
}

df = pd.DataFrame(data)

print("=" * 60)
print("            IPL CRICKET ANALYTICS REPORT")
print("=" * 60)

print("\n== Player Dataset ==")
print(df)

top_scorer = df.loc[df["Runs"].idxmax()]
print("\n== TOP SCORER ==")
print(f"Player : {top_scorer['Player']}")
print(f"Runs   : {top_scorer['Runs']}")
print(f"Team   : {top_scorer['Team']}")

average_runs = df["Runs"].mean()
print("\n== AVERAGE RUNS ==")
print(f"{average_runs:.2f}")

print("\n== TEAM-WISE ANALYSIS ==")
team_analysis = df.groupby("Team")["Runs"].sum()
print(team_analysis)

print("\n4. PLAYERS ABOVE AVERAGE RUNS")
above_average = df[df["Runs"] > average_runs]
print(above_average)

