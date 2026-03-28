import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datasets import load_dataset


dataset = load_dataset('lukebarousse/data_jobs')
df = dataset['train'].to_pandas()

df['job_posted_date'] = pd.to_datetime(df['job_posted_date'])

job_count = df['job_title_short'].value_counts().head(10)

plt.barh(job_count.index, job_count.values)
plt.xticks(rotation=45, ha='right', va='top')
plt.xlabel("Job Title")
plt.ylabel("Count")
plt.title("Top 10 Job Roles")

plt.show()