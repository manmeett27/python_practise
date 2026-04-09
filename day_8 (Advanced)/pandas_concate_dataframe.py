# Importing Libraries
import pandas as pd
from datasets import load_dataset
import matplotlib.pyplot as plt  

# Loading Data
dataset = load_dataset('lukebarousse/data_jobs')
df = dataset['train'].to_pandas()

# Data Cleanup
df['job_posted_date'] = pd.to_datetime(df['job_posted_date'])

# # Sample dataset of job postings in January
# job_postings_jan = pd.DataFrame({
#     'job_id': [1, 2, 3, 4, 5],
#     'job_title': ['Data Scientist', 'Data Analyst', 'Machine Learning Engineer', 'Data Scientist', 'Data Engineer'],
#     'company': ['Company A', 'Company B', 'Company C', 'Company D', 'Company E'],
#     'job_posted_date': pd.to_datetime(['2024-01-02', '2024-01-07', '2024-01-14', '2024-01-19', '2024-01-24'])
# })
# # Sample dataset of job postings in February
# job_postings_feb = pd.DataFrame({
#     'job_id': [6, 7, 8, 9, 10],
#     'job_title': ['Data Scientist', 'Data Analyst', 'Machine Learning Engineer', 'Data Scientist', 'Data Engineer'],
#     'company': ['Company F', 'Company G', 'Company H', 'Company I', 'Company J'],
#     'job_posted_date': pd.to_datetime(['2024-02-05', '2024-02-09', '2024-02-12', '2024-02-18', '2024-02-22'])
# })

# combine_jan_fab = pd.concat([job_postings_jan, job_postings_feb])
# print(combine_jan_fab)

df['job_posted_month'] = df['job_posted_date'].dt.strftime('%b')
months = df['job_posted_month'].unique()
print(months)
df_month = {month: df[df['job_posted_month'] == month] for month in months }

q1 = df_month['Jan'], df_month['Feb'], df_month['Mar']
combine_q1 = pd.concat(q1)
print(combine_q1)
counts = combine_q1['job_posted_month'].value_counts()
plt.barh(counts.index, counts.values)
plt.show()