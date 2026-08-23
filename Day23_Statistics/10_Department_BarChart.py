import pandas as pd
import matplotlib.pyplot as plt
employees={'Department':['IT','HR','IT','Finance','HR','Finance','IT'],'Salary':[50000,45000,60000,80000,55000,75000,65000]}
df=pd.DataFrame(employees)
d=df.groupby('Department')['Salary'].mean()
plt.bar(d.index,d.values)
plt.title('Average Salary by Department')
plt.show()
