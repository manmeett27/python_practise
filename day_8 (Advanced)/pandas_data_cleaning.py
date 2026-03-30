import pandas as pd
from datasets import load_dataset
import matplotlib.pyplot as plt  

# Loading Data
dataset = load_dataset('lukebarousse/data_jobs')
df = dataset['train'].to_pandas()

# Data Cleanup
df['job_posted_date'] = pd.to_datetime(df['job_posted_date'])

df_cleaned = df.dropna(how='all')
# df_cleaned.info()
# print(df_cleaned.iloc[:10,11:14])
df_filled = ['salary_rate', 'salary_year_avg', 'salary_hour_avg']
df_filled = df_cleaned.fillna(0)
# print(df_filled.iloc[:10,11:14])
df_unique = df_filled.drop_duplicates(subset=['job_title'])
print(df_unique.head(10))
