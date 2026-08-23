import seaborn as sns
import matplotlib.pyplot as plt

df=sns.load_dataset('flights')
sns.lineplot(data=df,x='year',y='passengers')
plt.title('Air Passengers Trend')
plt.show()