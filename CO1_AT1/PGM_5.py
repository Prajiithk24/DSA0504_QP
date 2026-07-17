import pandas as pd

df = pd.read_csv("../Csv/sales.csv")

print("Total Sales:", df["Sales"].sum())
print("Average Sales:", df["Sales"].mean())
print("Maximum Sales:", df["Sales"].max())
print("Minimum Sales:", df["Sales"].min())