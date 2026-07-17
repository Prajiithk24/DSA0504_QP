import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Csv/Lab6.csv")

df["Date"] = pd.to_datetime(df["Date"])

start_date = "2020-04-01"
end_date = "2020-05-01"

stock = df[(df["Date"] >= start_date) & (df["Date"] <= end_date)]

plt.figure(figsize=(8,5))
plt.scatter(stock["Volume"], stock["Close"])

plt.title("Trading Volume vs Stock Price of Alphabet Inc.")
plt.xlabel("Trading Volume")
plt.ylabel("Closing Stock Price")
plt.grid(True)

plt.show()