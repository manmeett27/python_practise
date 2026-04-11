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

# For Example purpose only
# data = {
#     'job_title_short': ['Data Analyst', 'Data Scientist', 'Data Engineer'],
#     'job_skills': [['excel', 'sql', 'python'], ['python', 'r'], ['aws', 'python', 'airflow']]
# }

# df_skills = pd.DataFrame(data)
# df_explode = df_skills.explode('job_skills')
# print(df_explode)
# df_explode.value_counts('job_skills').plot(kind='bar')
# plt.show()

df['job_skills'] = df['job_skills'].apply(lambda x: ast.literal_eval(x) if pd.notna(x) else x)

a= df[['job_title_short','job_skills']].head(5)
# print(a)
df_explode = a.explode('job_skills').head(10)
df_explode['job_skills'].value_counts('job_skills').plot(kind='bar')
plt.show()
