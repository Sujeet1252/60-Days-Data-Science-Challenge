import seaborn as sns
import matplotlib.pyplot as plt

df=sns.load_dataset('iris')
sns.heatmap(df.corr(numeric_only=True),annot=True)
plt.show()