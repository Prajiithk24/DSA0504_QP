import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Csv/Lab4.csv")

df["Date"] = pd.to_datetime(df["Date"])

start_date = "2022-01-05"
end_date = "2022-01-12"

stock = df[(df["Date"] >= start_date) & (df["Date"] <= end_date)]

plt.figure(figsize=(8,5))
plt.bar(stock["Date"].dt.strftime("%Y-%m-%d"), stock["Volume"])

plt.title("Trading Volume of Alphabet Inc.")
plt.xlabel("Date")
plt.ylabel("Trading Volume")
plt.xticks(rotation=45)

plt.show()