import matplotlib.pylab as plt
import seaborn as sns

# Tip amounts by day
tips = sns.load_dataset("tips")
sns.violinplot(data=tips,
              x="day", y="tip")
plt.show()