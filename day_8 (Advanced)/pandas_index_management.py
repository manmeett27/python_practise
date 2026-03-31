import pandas as pd
from datasets import load_dataset
import matplotlib.pyplot as plt

# Loading Data
dataset = load_dataset('lukebarousse/data_jobs')
df = dataset['train'].to_pandas()

# Data Cleanup
df['job_posted_date'] = pd.to_datetime(df['job_posted_date'])

# print(df.index.dtype)
df.index.name = 'index'
# print(df.index.name)

df_usa = df[df['job_country']=='United States']
# print(df_usa.reset_index(inplace=False))
# median_pivot.set_index('job_title_short', inplace=True)
# df.sort_index(inplace=True)