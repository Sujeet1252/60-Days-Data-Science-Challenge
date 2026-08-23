import pandas as pd
import matplotlib.pyplot as plt
df=pd.DataFrame({'Department':['IT','HR','IT','Finance','HR','IT']})
c=df['Department'].value_counts()
plt.bar(c.index,c.values)
plt.show()
