import pandas as pd
from datasets import load_dataset

# Loading Data
dataset = load_dataset('lukebarousse/data_jobs')
df = dataset['train'].to_pandas()

# Data Cleanup
df['job_posted_date'] = pd.to_datetime(df['job_posted_date'])

print(df.describe())

print(f"total salary {df['salary_year_avg'].sum()}")

print(df['job_title_short'].value_counts())


'''df.cumsum() - Cummulative sum of values
df.min()/df.max() - Minimum/maximum values
df.idxmin()/df.idxmax() - Indexes of minimum/Maximum value
df.mean() - Mean of values
df.median() - Median of values
df.mode() - Mode of the values'''