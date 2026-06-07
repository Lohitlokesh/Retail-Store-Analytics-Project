import pandas as pd

df = pd.read_csv("Data/Raw/store_sales_data.csv")

# Convert Date Columns

date_cols = [
    "Date of Birth",
    "Sales Date",
    "Order Date",
    "Ship Date"
]

for col in date_cols:
    df[col] = pd.to_datetime(df[col])

print(df.info())
print(df.dtypes)