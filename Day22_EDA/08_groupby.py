import seaborn as sns

df = sns.load_dataset('tips')
print(df.groupby('day')['total_bill'].mean())
