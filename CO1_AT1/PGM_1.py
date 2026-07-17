import pandas as pd

df = pd.read_csv("../Csv/Employee.csv")

print("Employees earning more than ₹50,000")
print(df[df["Salary"] > 50000])

print("\nAverage Salary Department-wise")
print(df.groupby("Department")["Salary"].mean())