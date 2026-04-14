import matplotlib.pylab as plt
import seaborn as sns

penguins = sns.load_dataset("penguins")
sns.histplot(data=penguins,
            x="body_mass_g")
sns.set_theme()
plt.show()