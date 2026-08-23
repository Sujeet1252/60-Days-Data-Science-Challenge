import pandas as pd
import matplotlib.pyplot as plt
df=pd.DataFrame({'Experience':[1,2,3,4,5],'Salary':[25000,30000,35000,45000,55000]})
plt.scatter(df['Experience'],df['Salary'])
plt.show()
