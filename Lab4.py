import pandas as pd
import matplotlib.pyplot as plt  # type: ignore

df = pd.read_csv("Csv/Lab4.csv")

df["Date"] = pd.to_datetime(df["Date"])
start_date = "2022-01-05"
end_date = "2022-01-12"

stock = df[(df["Date"] >= start_date) & (df["Date"] <= end_date)]

# Create line plot
plt.figure(figsize=(8,5))
plt.plot(stock["Date"], stock["Close"], marker="o")

plt.title("Historical Stock Prices of Alphabet Inc.")
plt.xlabel("Date")
plt.ylabel("Closing Price ($)")
plt.grid(True)
plt.xticks(rotation=45)

plt.show()