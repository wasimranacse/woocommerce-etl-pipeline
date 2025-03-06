-- SQL Queries for analysis

-- Monthly Sales Trend
SELECT 
    DATE_TRUNC('month', date) AS month, 
    SUM(net_sales) AS total_sales
FROM orders
GROUP BY month
ORDER BY month;


--  Top 5 Customers by Revenue

SELECT 
    customer, 
    SUM(net_sales) AS total_spent
FROM orders
GROUP BY customer
ORDER BY total_spent DESC
LIMIT 5;



-- Best-Selling Products

SELECT 
    UNNEST(string_to_array(products, ',')) AS product, 
    SUM(item_sold) AS total_sold
FROM orders
GROUP BY product
ORDER BY total_sold DESC
LIMIT 5;







