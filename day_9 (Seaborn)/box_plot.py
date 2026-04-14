import matplotlib.pylab as plt
import seaborn as sns

# Penguin flippers by species
penguins = sns.load_dataset("penguins")
sns.boxplot(data=penguins,
           x="species",
           y="flipper_length_mm")
sns.set_theme()
plt.show()