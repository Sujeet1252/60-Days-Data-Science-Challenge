import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.DataFrame({'Age':[20,22,24,26],'Salary':[25000,30000,35000,40000],'Experience':[1,2,3,4]})
sns.heatmap(df.corr(numeric_only=True),annot=True,cmap='Blues')
plt.show()
