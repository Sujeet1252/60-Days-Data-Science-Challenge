import seaborn as sns

df = sns.load_dataset('titanic')
print(df.info())
print(df.shape)
print(df.columns)
