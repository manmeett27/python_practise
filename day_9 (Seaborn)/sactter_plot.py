import matplotlib.pylab as plt
import seaborn as sns

# Do bigger bills get more tips?
tips = sns.load_dataset("tips")
sns.scatterplot(
    data=tips.sample(20),
    x="total_bill", y="tip", hue="day")
sns.set_theme()
plt.show()