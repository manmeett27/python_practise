import pandas as pd
from datasets import load_dataset
import matplotlib.pyplot as plt  

# Loading Data
dataset = load_dataset('lukebarousse/data_jobs')
df = dataset['train'].to_pandas()

# Data Cleanup
df['job_posted_date'] = pd.to_datetime(df['job_posted_date'])

# accessing by iloc[]
print(df.iloc[0])
print(df.iloc[0:10])
print(df.iloc[0,10])
print(df.iloc[[2,5][15,16]])
print(df.iloc[:,:5])

# accessing by loc[]
print(df.iloc[0])
print(df.iloc[:9,['job_skills','job_type_skills']])