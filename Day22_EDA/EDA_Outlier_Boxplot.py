import pandas as pd
import matplotlib.pyplot as plt
df=pd.DataFrame({'Salary':[25000,27000,26000,25500,100000]})
plt.boxplot(df['Salary'])
plt.title('Salary Boxplot')
plt.show()
