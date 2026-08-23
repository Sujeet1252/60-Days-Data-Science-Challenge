import pandas as pd
import matplotlib.pyplot as plt
df=pd.DataFrame({'Age':[20,21,22,23,24,25,26]})
plt.hist(df['Age'])
plt.show()
