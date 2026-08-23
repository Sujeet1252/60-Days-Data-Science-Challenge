import seaborn as sns

df=sns.load_dataset('titanic')
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())
print(df.nunique())
print(df.corr(numeric_only=True))
