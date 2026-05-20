#Total sales

SELECT SUM(sales) AS total_sales
FROM sales;

#Top 5 products
    
SELECT product_name,
       SUM(sales) AS total_sales
FROM sales
GROUP BY product_name
ORDER BY total_sales DESC
LIMIT 5;

#Region-wise Sales
    
SELECT region,
       SUM(sales) AS total_sales
FROM sales
GROUP BY region;

#Monthly Revenue
    
SELECT DATE_TRUNC('month', order_date) AS month,
       SUM(sales) AS revenue
FROM sales
GROUP BY month
ORDER BY month;