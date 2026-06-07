import pandas as pd

df = pd.read_csv("Data/Raw/store_sales_data.csv")

print("="*50)
print("UNIQUE VALUES")
print("="*50)

for col in df.columns:
    print(f"{col}: {df[col].nunique()}")

print("\nSTATE COUNT")
print(df["State"].nunique())

print("\nREGIONS")
print(df["Region"].unique())

print("\nSEGMENTS")
print(df["Segment"].unique())

print("\nSHIP MODES")
print(df["Ship Mode"].unique())

print("\nCATEGORY OF GOODS")
print(df["Category of Goods"].unique())