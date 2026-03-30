# Importing Libraries
import pandas as pd
from datasets import load_dataset
import matplotlib.pyplot as plt  
import pandas_data_management as dm

# Loading Data
dataset = load_dataset('lukebarousse/data_jobs')
df = dataset['train'].to_pandas()

# Data Cleanup
df['job_posted_date'] = pd.to_datetime(df['job_posted_date'])

# print(df.pivot_table(values='salary_year_avg', index='job_title_short', aggfunc='median'))

# print(df.pivot_table(index='job_title_short', aggfunc='size'))

# print(df.pivot_table(
#     values='salary_year_avg',
#     index=['job_country','job_title_short'],
#     aggfunc=['mean', 'median', 'count', 'min', 'max']).fillna(dm.median_salary))

df_job_country_salary = df.pivot_table(
    values='salary_year_avg',
    index='job_country',
    columns='job_title_short',
    aggfunc='median').fillna(dm.median_salary)

# print(df_job_country_salary)

# make a list of top 6 countries
top_countries = df['job_country'].value_counts().head(6).index

# filter df_job_country_salary for top 6 countries
df_job_country_salary = df_job_country_salary.loc[top_countries]

# filter df_job_country_salary for list of 6 job titles
job_titles = ['Data Analyst', 'Data Engineer', 'Data Scientist'] # 'Senior Data Analyst', 'Senior Data Engineer', 'Senior Data Scientist']
df_job_country_salary = df_job_country_salary[job_titles]

df_job_country_salary.plot(kind='bar')
plt.ylabel('Median Salary ($USD)')
plt.xlabel('')
plt.title('Median Salary by Country and Job Title')  
plt.xticks(rotation=45, ha='right')
plt.show()