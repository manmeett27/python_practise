'''Graph the average salary (salary_year_avg) by job_title_short as a horizontal bar chart. Order it from the highest salary to the lowest. Include a title, and labels for the x & y-axis.'''

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datasets import load_dataset


dataset = load_dataset('lukebarousse/data_jobs')
df = dataset['train'].to_pandas()

avg_salary = df.groupby('job_title_short')['salary_year_avg'].mean()
avg_salary = avg_salary.sort_index(ascending=False)
plt.barh(avg_salary.index, avg_salary.values)
plt.title("Average Salary by Job Title")
plt.xlabel("Average Salary")
plt.ylabel("Job Title")
plt.gca().invert_yaxis() 
plt.show()

'''Salaries often follow a skewed distribution where most employees earn on the lower end of the scale, and a few high earners pull the average (mean) up. In such cases, the mean does not accurately reflect the earnings of the majority.'''

job_salary = df.groupby('job_title_short')['salary_year_avg'].median().sort_values()
job_salary.plot(kind='barh')
plt.xlabel('Salary ($USD)')
plt.ylabel('')
plt.title('Median Salary by Job Title')
plt.show()