import pandas as pd

df = pd.read_csv(
    "Data/Raw/store_sales_data.csv"
)

date_cols = [
    "Date of Birth",
    "Sales Date",
    "Order Date",
    "Ship Date"
]

for col in date_cols:
    df[col] = pd.to_datetime(df[col])

today = pd.Timestamp.today()

df["Customer Age"] = (
    today.year -
    df["Date of Birth"].dt.year
)

df["Order Year"] = (
    df["Order Date"].dt.year
)

df["Order Month"] = (
    df["Order Date"].dt.month
)

df["Month Name"] = (
    df["Order Date"].dt.month_name()
)

df["Quarter"] = (
    df["Order Date"].dt.quarter
)

df["Day Name"] = (
    df["Order Date"].dt.day_name()
)

df["Shipping Days"] = (
    df["Ship Date"] -
    df["Order Date"]
).dt.days

df["Profit Margin %"] = (
    df["Profit"] /
    df["Sales"]
) * 100

df["Discount Amount"] = (
    df["Sales"] *
    df["Discount"]
)

df["Sales Bucket"] = pd.cut(
    df["Sales"],
    bins=[0,10000,20000,30000,40000,50000],
    labels=[
        "Very Low",
        "Low",
        "Medium",
        "High",
        "Very High"
    ]
)

print(df.head())

print("\nNew Shape:")
print(df.shape)

df.to_csv(
    "Data/Cleaned/store_sales_cleaned.csv",
    index=False
)