import pandas as pd
df=pd.DataFrame({'Name':['A','B','A'],'Marks':[90,80,90]})
print(df)
print(df.duplicated().sum())
print(df.drop_duplicates())
