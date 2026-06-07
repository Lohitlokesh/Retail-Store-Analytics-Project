import pandas as pd
import numpy as np
df = pd.read_csv("Data/Raw/store_sales_data.csv")

# First 5 Rows
print("\nFIRST 5 ROWS")
print(df.head())

# Shape
print("\nDATASET SHAPE")
print(df.shape)

# Columns
print("\nCOLUMN NAMES")
print(df.columns)

# Info
print("\nDATASET INFO")
df.info()

# Summary Statistics
print("\nSUMMARY STATISTICS")
print(df.describe())

# Missing Values
print("\nMISSING VALUES")
print(df.isnull().sum())

# Duplicates
print("\nDUPLICATES")
duplicates = df.duplicated()
print(duplicates.sum())

# Unique Values
print("\nUNIQUE VALUES")
for col in df.columns:
    print(f"\n{col}")
    print(df[col].nunique())