# Exercise - Investigating Trending Skills


# Topics Covered
# This exercise goes over:

# Applying Functions
# Exploding
# Pivoting
# Plotting


# Question
# How are skills trending for Data Analysts on a monthly basis.


# Importing Libraries
import ast
import pandas as pd
from datasets import load_dataset
import matplotlib.pyplot as plt  

# Loading Data
dataset = load_dataset('lukebarousse/data_jobs')
df = dataset['train'].to_pandas()

# Data Cleanup
df['job_posted_date'] = pd.to_datetime(df['job_posted_date'])
df['job_skills'] = df['job_skills'].apply(lambda x: ast.literal_eval(x) if pd.notna(x) else x);


df_DA = df[df['job_title_short']=='Data Analyst'].copy()
df_DA['job_posted_month'] = df_DA['job_posted_date'].dt.month
df_explode = df_DA.explode('job_skills')
df_pivot_table = df_explode.pivot_table(index='job_posted_month', columns='job_skills', aggfunc='size', fill_value=0)

# note
# You created the column in df_DA after exploding:
# But df_DA_explode was created before the new column was added.
# So the exploded dataframe doesn't contain job_posted_month_no, which causes the KeyError.

print(df_pivot_table)