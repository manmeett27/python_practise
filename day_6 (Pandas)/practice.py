from datasets import load_dataset
data = load_dataset('lukebarousse/data_jobs')
df = data['train'].to_pandas()
print(df[df['salary_year_avg'].notna()])