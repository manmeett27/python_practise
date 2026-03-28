from datasets import load_dataset
data = load_dataset('lukebarousse/data_jobs')
df = data['train'].to_pandas()

print(df.head())  
# Shows first 5 rows of the dataset

print(df.tail())  
# Shows last 5 rows of the dataset

df.info()  
# Gives summary: columns, data types, non-null values

print(df.describe())  
# Shows statistics (mean, min, max, etc.) for numeric columns

print(df['City'].unique())  
# Shows all unique values in 'City' column

print(df['Name'])  
# Selects and prints the 'Name' column

print(df.iloc[0:2])  
# Selects first 2 rows (index 0 and 1)

print(df.dropna())  
# Removes rows where ANY value is missing (NA)

print(df.dropna(subset=['Age']))  
# Removes rows where 'Age' column has missing values

print(df.isna())  
# Shows True/False for missing values in each cell

print(df[df['salary_year_avg'].notna()])  
# Filters rows where 'salary_year_avg' is NOT missing