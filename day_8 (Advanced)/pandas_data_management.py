import pandas as pd
from datasets import load_dataset
import matplotlib.pyplot as plt  

# Loading Data
dataset = load_dataset('lukebarousse/data_jobs')
df = dataset['train'].to_pandas()

# Data Cleanup
df['job_posted_date'] = pd.to_datetime(df['job_posted_date'])

# DataFrame Copy
df_original = df.copy()

# Create new dataframe
df_altered = df_original.copy()

# Calculating the median salary
median_salary = df_altered['salary_year_avg'].median()

# Filling the missing values with the median salary
df_altered['salary_year_avg'] = df_altered.loc[:,'salary_year_avg'].fillna(median_salary)

# print(df_original.loc[:5,'salary_year_avg'])
# print(df_altered.loc[:5,'salary_year_avg'])

# print(df.sample(n=5))
print(df.sample(frac=0.1, replace=False))