import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.histplot(data=tips, x="total_bill", kde=True)
plt.title("Distribution of Total Bill")
plt.show()
