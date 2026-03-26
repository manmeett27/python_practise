'''The Scenario: You have a list of exam scores for 100 students across 3 subjects (Math, Science, English).
data = np.random.randint(0, 100, (100, 3))

The Tasks:

Calculate the average score for each student (across the rows).

Calculate the highest score for each subject (across the columns).

The "Bonus": Find how many students scored above 90 in all three subjects at the same time.'''

import numpy as np
data = np.random.randint(0, 100, (100, 3))
average = data.mean(axis=1)
highest_max = data.max(axis=0)

std = np.all(data>90,axis=1)
print(f"Number Of Students got marks more than 90: {np.sum(std)}")