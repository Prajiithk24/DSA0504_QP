import pandas as pd

data = pd.read_csv('Csv/Lab2.csv')

result = data.groupby("EMPLOYEE_ID").filter(lambda x: len(x) >= 2).sort_values(by="EMPLOYEE_ID")

print("Employees who have done two or more jobs:")
print(result)
