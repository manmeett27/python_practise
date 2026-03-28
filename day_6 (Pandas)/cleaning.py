import pandas as pd
from datasets import load_dataset
data = load_dataset('lukebarousse/data_jobs')
df = data['train'].to_pandas()
df['job_posted_date'] = pd.to_datetime(df['job_posted_date'])
df['job_posted_date'] = df['job_posted_date'].dt.date
df.sort_values(by='job_posted_date', ascending=False, inplace=True)
df.drop('salary_hour_avg', axis = 1, inplace=True)
df.dropna(subset=['salary_year_avg'], inplace=True)
print(df.head())