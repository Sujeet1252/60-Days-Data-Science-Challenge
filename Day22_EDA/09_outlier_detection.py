import seaborn as sns

df = sns.load_dataset('tips')
q1=df['total_bill'].quantile(0.25)
q3=df['total_bill'].quantile(0.75)
iqr=q3-q1
print('Q1=',q1,'Q3=',q3,'IQR=',iqr)
