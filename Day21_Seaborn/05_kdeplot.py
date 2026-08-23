import seaborn as sns
import matplotlib.pyplot as plt

df=sns.load_dataset('penguins')
sns.kdeplot(data=df,x='body_mass_g',fill=True)
plt.title('KDE Plot')
plt.show()