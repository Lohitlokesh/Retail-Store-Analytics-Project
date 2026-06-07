import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(
    style="whitegrid",
    palette="deep"
)

df = pd.read_csv(
    "Data/Cleaned/store_sales_cleaned.csv"
)

# Sales Distribution

plt.figure(figsize=(10,5))
sns.histplot(
    data=df,
    x="Sales",
    bins=30,
    kde=True
)
plt.title("Sales Distribution")
plt.savefig(
    "Reports/Charts/1.sales_distribution.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()

# Profit Distribution

plt.figure(figsize=(10,5))
sns.histplot(
    data=df,
    x="Profit",
    bins=30,
    kde=True
)
plt.title("Profit Distribution")
plt.savefig(
    "Reports/Charts/2.profit_distribution.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()

# Monthly Sales Trend

month_order = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

monthly_sales = (
    df.groupby("Month Name")["Sales"]
      .sum()
      .reindex(month_order)
)

plt.figure(figsize=(12,6))
monthly_sales.plot(
    marker="o"
)
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.savefig(
    "Reports/Charts/3.monthly_sales.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()

# Category Performance

category_sales = (
    df.groupby("Category of Goods")["Sales"]
      .sum()
      .sort_values()
)

plt.figure(figsize=(10,6))
category_sales.plot(
    kind="barh"
)
plt.title("Sales by Category")
plt.savefig(
    "Reports/Charts/4.category_performance.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()

# Top 10 States

top_states = (
    df.groupby("State")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

plt.figure(figsize=(12,6))
sns.barplot(
    x=top_states.values,
    y=top_states.index
)
plt.title("Top States by Sales")
plt.savefig(
    "Reports/Charts/5.top10_states.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()

# Region Analysis

region_sales = (
    df.groupby("Region")["Sales"]
      .sum()
)

plt.figure(figsize=(8,8))
plt.pie(
    region_sales,
    labels=region_sales.index,
    autopct="%1.1f%%"
)
plt.title("Sales by Region")
plt.savefig(
    "Reports/Charts/6.region_analysis.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()

# Segment Analysis

segment_sales = (
    df.groupby("Segment")["Sales"]
      .sum()
)

plt.figure(figsize=(7,7))
plt.pie(
    segment_sales,
    labels=segment_sales.index,
    autopct="%1.1f%%"
)
plt.title("Sales by Segment")
plt.savefig(
    "Reports/Charts/7.segment_analysis.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()

# Ship Mode Analysis

ship_sales = (
    df.groupby("Ship Mode")["Sales"]
      .sum()
      .sort_values()
)

plt.figure(figsize=(10,5))
ship_sales.plot(kind="bar")
plt.title("Sales by Ship Mode")
plt.savefig(
    "Reports/Charts/8.ship_mode.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()

# Shipping Days Analysis

plt.figure(figsize=(10,5))
sns.boxplot(
    x=df["Shipping Days"]
)
plt.title("Shipping Days Distribution")
plt.savefig(
    "Reports/Charts/9.shipping_days.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()

# Correlation Heatmap

numeric_cols = [
    "Sales",
    "Profit",
    "Quantity",
    "Discount",
    "Shipping Days",
    "Profit Margin %",
    "Customer Age"
]

plt.figure(figsize=(10,8))
sns.heatmap(
    df[numeric_cols].corr(),
    annot=True,
    cmap="coolwarm"
)
plt.title("Correlation Matrix")
plt.savefig(
    "Reports/Charts/10.correlation_heatmap.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()