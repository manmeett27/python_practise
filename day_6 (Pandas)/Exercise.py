'''
Question 1. 
Perform an exploratory analysis focusing on data jobs in each country. Look at the average yearly salary, job count, and salary range (minimum and maximum salaries).'''


import pandas as pd
from datasets import load_dataset

data = load_dataset('lukebarousse/data_jobs')

df = data['train'].to_pandas()

print(df.groupby('job_country').agg({
    'salary_year_avg': ['min', 'max'],
    'job_title_short': 'count'
}))

'''
Question 2.
Count the total number of data analyst job postings for each job title to understand the job market size.

We're using size() to get a straightforward count of all postings per job title (including those will nulls in other columns but not the country column).'''

df.groupby('job_title_short').size().sort_values(ascending=False)

'''
Question 3.
Determine the minimum and maximum yearly salaries offered in each job title to assess the salary range and economic disparity.

We use agg() because we want to get both the min and max salary_year_avg by job_title_short.'''

df.groupby('job_title_short')['salary_year_avg'].agg(['median', 'min', 'max', 'count']).sort_values(by='median', ascending=False)