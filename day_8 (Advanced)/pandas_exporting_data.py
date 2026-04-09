# Importing Libraries
import pandas as pd
from datasets import load_dataset
import matplotlib.pyplot as plt  

# Loading Data
dataset = load_dataset('lukebarousse/data_jobs')
df = dataset['train'].to_pandas()

# Data Cleanup
df['job_posted_date'] = pd.to_datetime(df['job_posted_date'])

# to_csv(): Export DataFrame to CSV file.
# to_excel(): Export DataFrame to Excel file.
# Then, is writing to a SQL database. This will only work if you actually have a database to write to. In our case we don't, so this is just an example.

# # saving the DataFrame to a SQL database

# # this requires a connection to a SQL database, we'll use sqlalchemy for this
# # !conda install -c anaconda sqlalchemy -y
# from sqlalchemy import create_engine
# engine = create_engine('sqlite:///jobs.db')

# df.to_sql('job_table', con=engine, if_exists='append', index=False)
# to_parquet(): Export DataFrame to a parquet file.