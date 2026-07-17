import pandas as pd

df = pd.read_csv("../Csv/student.csv")

print("Missing Values")
print(df.isnull())

df.fillna(df.mean(numeric_only=True), inplace=True)

print("\nCleaned Dataset")
print(df)