import pandas as pd

df = pd.read_csv("../Csv/customer.csv")

print("Duplicate Records")
print(df[df.duplicated()])

df = df.drop_duplicates()

print("\nUpdated Dataset")
print(df)