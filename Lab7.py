import pandas as pd

df = pd.read_csv("Csv/Lab7.csv")

pivot = pd.pivot_table(
    df,
    index="Item",
    values="Sale_amt",
    aggfunc=["max", "min"]
)

print(pivot)