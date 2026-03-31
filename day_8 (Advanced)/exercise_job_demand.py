'''Question
In our project we want to see how in-demand skills are trending for data jobs. But before we do that let's look at:

General trend of data jobs in demand. We're going to look at it by month.'''


import pandas as pd
from datasets import load_dataset
import matplotlib.pyplot as plt  

# Loading Data
dataset = load_dataset('lukebarousse/data_jobs')
df = dataset['train'].to_pandas()

# Data Cleanup
df['job_posted_date'] = pd.to_datetime(df['job_posted_date'])


df_US_pivot = df.copy()

df_US_pivot['job_posted_month'] = df_US_pivot['job_posted_date'].dt.strftime('%B')
df_US_pivot['job_posted_month_no'] = df_US_pivot['job_posted_date'].dt.month

df_US_pivot = df_US_pivot.sort_values('job_posted_month_no')

df_pivot_table = df_US_pivot.pivot_table(
    index='job_posted_month',
    columns='job_title_short',
    aggfunc='size'
)

df_pivot_table.plot(kind='line', figsize=(10,6))
plt.show()