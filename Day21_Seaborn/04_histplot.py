import seaborn as sns
import matplotlib.pyplot as plt

df=sns.load_dataset('penguins')
sns.histplot(data=df,x='flipper_length_mm',kde=True)
plt.title('Histogram')
plt.show()