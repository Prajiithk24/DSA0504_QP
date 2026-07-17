import pandas as pd

df = pd.read_csv("../Csv/product.csv")

exchange_rate = 83

df["Price_INR"] = df["Price_USD"] * exchange_rate

print(df)