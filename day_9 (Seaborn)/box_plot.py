import matplotlib.pylab as plt
import seaborn as sns


# Show average tip by day
tips = sns.load_dataset("tips")
sns.barplot(data=tips,
           x="day", y="tip")
sns.set_theme()
plt.show()