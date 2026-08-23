import seaborn as sns

df=sns.load_dataset('iris')
sns.pairplot(df,hue='species')