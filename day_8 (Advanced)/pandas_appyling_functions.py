# Importing Libraries
import pandas as pd
from datasets import load_dataset
import matplotlib.pyplot as plt  
import ast

# Loading Data
dataset = load_dataset('lukebarousse/data_jobs')
df = dataset['train'].to_pandas()

# Data Cleanup
df['job_posted_date'] = pd.to_datetime(df['job_posted_date'])

def inflated(salary):
    return salary*1.03

df['salary_year_inflated'] = df['salary_year_avg'].apply(inflated)

# print(df[pd.notna(df['salary_year_avg'])][['job_title_short','salary_year_avg', 'salary_year_inflated']])

def projected_salary(row):
    if 'Senior' in row['job_title_short']:
        return  1.05 * row['salary_year_avg']
    else:
        return  1.03 * row['salary_year_avg']

df['salary_year_inflated'] = df.apply(projected_salary, axis=1)

# print(df[pd.notna(df['salary_year_avg'])][['job_title_short', 'salary_year_avg', 'salary_year_inflated']])


# Convert string representation to actual list, checking for NaN values first
df['job_skills'] = df['job_skills'].apply(lambda x: ast.literal_eval(x) if pd.notna(x) else x)

print(df['job_skills'])