import pandas as pd

df = pd.read_csv("../Csv/Employee.csv")

result = df.groupby("Department")["Salary"].agg(
    Total_Salary="sum",
    Average_Salary="mean",
    Employee_Count="count"
)

print(result)
