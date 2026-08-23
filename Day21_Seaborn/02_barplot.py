import seaborn as sns
import matplotlib.pyplot as plt

df=sns.load_dataset('tips')
sns.barplot(data=df,x='day',y='total_bill')
plt.title('Average Bill by Day')
plt.show()