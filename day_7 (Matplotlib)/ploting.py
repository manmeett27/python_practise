import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datasets import load_dataset

# example
'''x = np.arange(0,5,0.1)
y = np.sin(x)
plt.plot(x,y)
plt.show()'''


dataset = load_dataset('lukebarousse/data_jobs')
df = dataset['train'].to_pandas()

df['job_posted_date'] = pd.to_datetime(df['job_posted_date'])

plt.plot(df['job_posted_date'], df['job_posted_date'])
plt.show()

date_count = df['job_posted_date'].value_counts()
date_count = date_count.sort_index()
print(date_count)

plt.plot(date_count.index, date_count.values)
plt.xlabel("Date")
plt.ylabel("Number of Jobs")
plt.title("Job Postings Over Time")
plt.show()


montly_counts = df.groupby(df['job_posted_date'].dt.to_period('M')).size()
montly_counts = montly_counts.sort_index()
plt.plot(montly_counts.index, montly_counts.values)
plt.show()

