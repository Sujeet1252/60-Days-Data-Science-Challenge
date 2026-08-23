import seaborn as sns
import matplotlib.pyplot as plt

df=sns.load_dataset('tips')
sns.scatterplot(data=df,x='total_bill',y='tip',hue='time')
plt.show()