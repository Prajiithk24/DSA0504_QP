import pandas as pd
data = pd.read_csv('Csv/Lab3.csv')
result = data.sort_values(by="JOB_TITLE", ascending=False)

print(result)