-- Total Sales
SELECT
    ROUND(SUM(sales),2) AS total_sales
FROM retail_sales;

-- Total Profit
SELECT
    ROUND(SUM(profit),2) AS total_profit
FROM retail_sales;

-- Average Order Value
SELECT
    ROUND(AVG(sales),2) AS average_order_value
FROM retail_sales;

-- Total Orders
SELECT
    COUNT(order_id) AS total_orders
FROM retail_sales;

-- Top 10 States by Sales
SELECT
    state,
    ROUND(SUM(sales),2) AS total_sales
FROM retail_sales
GROUP BY state
ORDER BY total_sales DESC
LIMIT 10;

-- Sales by Region
SELECT
    region,
    ROUND(SUM(sales),2) AS total_sales
FROM retail_sales
GROUP BY region
ORDER BY total_sales DESC;

-- Sales by Category
SELECT
    category_of_goods,
    ROUND(SUM(sales),2) AS total_sales
FROM retail_sales
GROUP BY category_of_goods
ORDER BY total_sales DESC;

-- Top 10 Sub-Categories
SELECT
    sub_category,
    ROUND(SUM(sales),2) AS total_sales
FROM retail_sales
GROUP BY sub_category
ORDER BY total_sales DESC
LIMIT 10;

-- Monthly Sales Trend
SELECT
    month_name,
    ROUND(SUM(sales),2) AS total_sales
FROM retail_sales
GROUP BY month_name
ORDER BY total_sales DESC;

-- Average Shipping Days
SELECT
    ROUND(AVG(shipping_days),2) AS avg_shipping_days
FROM retail_sales;

-- Top 10 Customers by Revenue
SELECT
    customer_id,
    customer_name,
    ROUND(SUM(sales),2) AS total_sales
FROM retail_sales
GROUP BY customer_id, customer_name
ORDER BY total_sales DESC
LIMIT 10;

-- Customer Ranking Using RANK()
SELECT
    customer_id,
    customer_name,
    SUM(sales) AS total_sales,
    RANK() OVER(
        ORDER BY SUM(sales) DESC
    ) AS sales_rank
FROM retail_sales
GROUP BY customer_id, customer_name;

-- State Ranking Using DENSE_RANK()
SELECT
    state,
    SUM(sales) AS total_sales,
    DENSE_RANK() OVER(
        ORDER BY SUM(sales) DESC
    ) AS state_rank
FROM retail_sales
GROUP BY state;

-- Sales Performance Classification
SELECT
    state,
    ROUND(SUM(sales),2) AS total_sales,
    CASE
        WHEN SUM(sales) > 252000000
            THEN 'High Performer'
        WHEN SUM(sales) > 248000000
            THEN 'Medium Performer'
        ELSE 'Low Performer'
    END AS performance_level
FROM retail_sales
GROUP BY state;