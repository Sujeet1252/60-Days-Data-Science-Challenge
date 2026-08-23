import pandas as pd
import numpy as np
employees={'Employee':['Aman','Rahul','Priya','Neha','Rohit','Simran','Karan'],'Department':['IT','HR','IT','Finance','HR','Finance','IT'],'Salary':[50000,45000,60000,80000,55000,75000,65000]}
df=pd.DataFrame(employees)
print(df)
print('Average:',df['Salary'].mean())
print('Median:',df['Salary'].median())
print('Max:',df['Salary'].max())
print('Min:',df['Salary'].min())
print('Range:',df['Salary'].max()-df['Salary'].min())
print('Variance:',np.var(df['Salary']))
print('Std:',np.std(df['Salary']))
