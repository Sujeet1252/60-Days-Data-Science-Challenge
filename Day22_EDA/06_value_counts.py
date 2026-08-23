import seaborn as sns

df = sns.load_dataset('titanic')
print(df['class'].value_counts())
