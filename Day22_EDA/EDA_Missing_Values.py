import pandas as pd
data={'Name':['A','B',None],'Marks':[90,None,80]}
df=pd.DataFrame(data)
print(df)
print(df.isnull().sum())
df['Marks']=df['Marks'].fillna(df['Marks'].mean())
df['Name']=df['Name'].fillna('Unknown')
print(df)
