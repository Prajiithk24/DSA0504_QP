import pandas as pd

data = pd.read_csv('Csv/Lab1.csv')

distinct_id = data['DEPARTMENT_ID'].unique()

print("Distinct Department IDs:")
print(distinct_id)
