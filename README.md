# 🛒 Retail Store Analytics Dashboard

## 📌 Project Overview

The **Retail Store Analytics Dashboard** is an end-to-end Data Analytics project built using **Python, MySQL, and Power BI**. The project focuses on analyzing retail sales data to uncover business insights related to sales performance, profitability, customer behavior, product categories, regions, and shipping operations.

This project demonstrates the complete Data Analytics workflow:

- Data Cleaning
- Feature Engineering
- Exploratory Data Analysis (EDA)
- SQL Analysis
- Interactive Dashboard Development
- Business Insights Generation

---

## 🎯 Objectives

- Analyze overall sales and profit performance.
- Identify top-performing regions, states, and product categories.
- Understand customer and segment contributions.
- Evaluate shipping performance.
- Build an interactive Power BI dashboard for business decision-making.

---

## 🛠️ Tech Stack

### Programming & Analysis
- Python
- Pandas
- NumPy

### Data Visualization
- Matplotlib
- Seaborn

### Database
- MySQL

### Business Intelligence
- Power BI

### Development Tools
- VS Code
- Git
- GitHub

---

## 📂 Project Structure

```text
Retail-Store-Analytics-Project/

│
├── Data/
│   ├── Raw/
│          └── store_sales_data.csv
│   └── Cleaned/
│          └── store_sales_cleaned.csv
├── Python/
│   ├── 01_data_loading.py
│   ├── 02_data_understanding.py
│   ├── 03_data_cleaning.py
│   ├── 04_feature_engineering.py
│   ├── 05_eda.py
│
├── SQL/
│   └── retail_analysis_queries.sql
│
├── PowerBI/
│   └── Retail_Store_Analytics.pbix
│
├── Reports/
│   └── Charts/
│         └── 1.sales_distributions.png
│         └── 2.profit_distribution.png
│         └── 3.monthly_sales.png
│         └── 4.category_performance.png
│         └── 5.top10_states.png
│         └── 6.region_analysis.png
│         └── 7.segment_analysis.png
│         └── 8.ship_mode.png
│         └── 9.shipping_days.png
│         └── 10.correlation_heatmap.png
│
└── README.md
```

---

## 📊 Dataset Information

### Raw Dataset

- Records: 100,000
- Columns: 25

### Cleaned Dataset

- Records: 100,000
- Columns: 35

### Additional Features Created

- Customer Age
- Order Year
- Order Month
- Month Name
- Quarter
- Day Name
- Shipping Days
- Profit Margin %
- Discount Amount
- Sales Bucket

---

## 🧹 Data Cleaning Process

The following preprocessing steps were performed:

- Converted date columns into datetime format.
- Checked missing values.
- Removed duplicate records.
- Standardized column formats.
- Validated data types.

---

## ⚙️ Feature Engineering

New business-related features were generated:

```python
Customer Age
Order Year
Order Month
Month Name
Quarter
Day Name
Shipping Days
Profit Margin %
Discount Amount
Sales Bucket
```

These features enhanced business analysis and reporting capabilities.

---

## 📈 Exploratory Data Analysis (EDA)

The following analyses were performed using Matplotlib and Seaborn:

### KPI Analysis

- Total Sales
- Total Profit
- Average Order Value
- Total Orders
- Profit Margin %

### Sales Analysis

- Monthly Sales Trend
- Region-wise Sales
- State-wise Sales
- Category Performance
- Sub-Category Performance

### Customer Analysis

- Segment Analysis
- Customer Age Analysis

### Shipping Analysis

- Shipping Mode Performance
- Average Shipping Days

### Correlation Analysis

- Correlation Heatmap
- Relationship between Sales, Profit, Discount, Quantity, Shipping Days, and Profit Margin

---

## 🗄️ SQL Analysis

The cleaned dataset was imported into MySQL and analyzed using SQL queries.

### SQL Tasks Performed

- Total Sales Calculation
- Total Profit Calculation
- Average Order Value
- Top 10 States by Sales
- Sales by Region
- Sales by Category
- Top Sub-Categories
- Monthly Sales Trends
- Average Shipping Days

---

## 📊 Power BI Dashboard

The final dashboard was built using Power BI and includes:

### KPI Cards

- Total Sales
- Total Profit
- Total Orders
- Average Order Value
- Profit Margin %

### Interactive Slicers

- Year
- Region

### Visualizations

- Monthly Sales Trend
- Sales by Region
- Sales by Segment
- Sales by Category
- Top 10 States by Sales
- Sales by Ship Mode
- Top 10 Sub-Categories

---

## 🔍 Key Business Insights

### Sales Performance

- Highest Sales Month: **May**
- Lowest Sales Month: **February**

### Regional Performance

- Top Region: **East**
- Contribution: **25.33%**

### State Performance

Top States by Sales:

1. Rajasthan
2. Punjab
3. Maharashtra

### Category Performance

- Highest Sales Category:
  - Sessional Fruits & Vegetables

- Lowest Sales Category:
  - Furniture

### Segment Analysis

- Consumer: 49.96%
- Corporate: 50.04%

### Shipping Analysis

- Highest Performing Ship Mode:
  - Same Day

### Correlation Analysis

- Strong Positive Correlation:
  - Sales ↔ Profit (0.82)

- Moderate Positive Correlation:
  - Profit ↔ Profit Margin (0.50)

- Moderate Negative Correlation:
  - Discount ↔ Profit Margin (-0.55)

---

## 📸 Dashboard Preview

Add your dashboard screenshot here:

```markdown
![Dashboard](Dashboard_Screenshot/dashboard.png)
```

---

## 🚀 Skills Demonstrated

### Data Analytics

- Data Cleaning
- Data Wrangling
- Feature Engineering
- Exploratory Data Analysis

### Programming

- Python
- Pandas
- NumPy

### Data Visualization

- Matplotlib
- Seaborn
- Power BI

### Database

- MySQL
- SQL Query Writing

### Business Intelligence

- KPI Development
- Dashboard Design
- Business Insight Generation

---

## 📚 Learning Outcomes

Through this project I gained practical experience in:

- Building end-to-end Data Analytics projects.
- Transforming raw data into actionable insights.
- Performing SQL-based business analysis.
- Creating professional Power BI dashboards.
- Applying real-world data analysis workflows used in industry.

---

## 👨‍💻 Author

**THAMAGONDA LOHIT KUMAR**

GitHub: https://github.com/Lohitlokesh

Project Repository:
https://github.com/Lohitlokesh/Retail-Store-Analytics-Project
---

