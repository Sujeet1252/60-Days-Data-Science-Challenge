import seaborn as sns
import matplotlib.pyplot as plt
salary=[50000,45000,60000,80000,55000,75000,65000]
sns.boxplot(x=salary)
plt.title('Salary Boxplot')
plt.show()
