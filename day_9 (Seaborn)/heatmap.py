import matplotlib.pylab as plt
import seaborn as sns

flights = sns.load_dataset("flights")
pivot = flights.pivot(index="month", columns="year", values="passengers")

sns.heatmap(pivot, annot=True, fmt="d", cmap="Blues")
plt.title("Flight Passengers per")
sns.set_theme()
plt.show()