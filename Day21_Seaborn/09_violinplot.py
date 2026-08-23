import seaborn as sns
import matplotlib.pyplot as plt

df=sns.load_dataset('tips')
sns.violinplot(data=df,x='day',y='total_bill')
plt.show()