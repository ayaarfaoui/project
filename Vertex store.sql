CREATE TABLE bi_project.product (
    product_id VARCHAR(50) PRIMARY KEY,
    category VARCHAR(50),
    sub_category VARCHAR(50),
    product_name VARCHAR(255)
);
CREATE TABLE bi_project.date (
    order_id VARCHAR(50) PRIMARY KEY,
    order_date DATE,
    ship_date DATE,
    year INT,
    month VARCHAR(20),
    quarter VARCHAR(20)
);
CREATE TABLE bi_project.customer (
    customer_id VARCHAR(50) PRIMARY KEY,
    customer_name VARCHAR(255),
    segment VARCHAR(50),
    state VARCHAR(50),
    country VARCHAR(50),
    market VARCHAR(50),
    region VARCHAR(50),
    order_priority VARCHAR(20)
);
CREATE TABLE bi_project.fact_sales (
    sale_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id VARCHAR(50),
    product_id VARCHAR(50),
    customer_id VARCHAR(50),
    sales DECIMAL(10, 2),
    profit DECIMAL(10, 2),
    discount DECIMAL(5, 2),
    quantity INT,
    shipping_cost DECIMAL(10, 2),
    FOREIGN KEY (order_id) REFERENCES date(order_id),
    FOREIGN KEY (product_id) REFERENCES product(product_id),
    FOREIGN KEY (customer_id) REFERENCES customer(customer_id)
);
-- Annual Sales Revenue View
CREATE VIEW bi_project.annual_sales_revenue AS
SELECT 
    bi_project.date.year AS sales_year, 
    SUM(bi_project.fact_sales.sales) AS total_revenue
FROM 
    bi_project.fact_sales
JOIN 
    bi_project.date ON bi_project.fact_sales.order_id = bi_project.date.order_id
GROUP BY 
    bi_project.date.year;
select * from bi_project.annual_sales_revenue;
-- Quarterly Sales Revenue View
CREATE VIEW bi_project.quarterly_sales_revenue AS
SELECT 
    bi_project.date.year AS sales_year, 
    bi_project.date.quarter AS sales_quarter, 
    SUM(bi_project.fact_sales.sales) AS total_revenue
FROM 
    bi_project.fact_sales
JOIN 
    bi_project.date ON bi_project.fact_sales.order_id = bi_project.date.order_id
GROUP BY 
    bi_project.date.year, bi_project.date.quarter;
select * from bi_project.quarterly_sales_revenue;

-- Monthly Sales Revenue View
CREATE VIEW bi_project.monthly_sales_revenue AS
SELECT 
    bi_project.date.year AS sales_year, 
    bi_project.date.month AS sales_month, 
    SUM(bi_project.fact_sales.sales) AS total_revenue
FROM 
    bi_project.fact_sales
JOIN 
    bi_project.date ON bi_project.fact_sales.order_id = bi_project.date.order_id
GROUP BY 
    bi_project.date.year, bi_project.date.month;
select * from bi_project.monthly_sales_revenue;
-- Top 10 countries by sales quantity
CREATE VIEW bi_project.top_10_countries_sales_quantity AS
SELECT 
    bi_project.customer.country AS customer_country, 
    SUM(bi_project.fact_sales.quantity) AS total_sales_quantity
FROM 
    bi_project.fact_sales
JOIN 
    bi_project.customer ON bi_project.fact_sales.customer_id = bi_project.customer.customer_id
GROUP BY 
    bi_project.customer.country
ORDER BY 
    total_sales_quantity DESC
LIMIT 10;
select * from bi_project.top_10_countries_sales_quantity;
-- Most profitable region by country in 2024
CREATE VIEW bi_project.regional_performance_2024 AS
SELECT 
    bi_project.customer.country AS customer_country, 
    bi_project.customer.region AS customer_region, 
    SUM(bi_project.fact_sales.profit) AS total_profit
FROM 
    bi_project.fact_sales
JOIN 
    bi_project.customer ON bi_project.fact_sales.customer_id = bi_project.customer.customer_id
JOIN 
    bi_project.date ON bi_project.fact_sales.order_id = bi_project.date.order_id
WHERE 
    bi_project.date.year = 2024
GROUP BY 
    bi_project.customer.country, bi_project.customer.region
ORDER BY 
    bi_project.customer.country, total_profit DESC;
select * from bi_project.regional_performance_2024;
-- Top 10 customers by purchase frequency
CREATE VIEW bi_project.top_10_customers_by_frequency AS
SELECT 
    bi_project.customer.customer_name AS customer_name, 
    COUNT(bi_project.fact_sales.sale_id) AS purchase_frequency
FROM 
    bi_project.fact_sales
JOIN 
    bi_project.customer ON bi_project.fact_sales.customer_id = bi_project.customer.customer_id
GROUP BY 
    bi_project.customer.customer_name
ORDER BY 
    purchase_frequency DESC
LIMIT 10;
select * from bi_project.top_10_customers_by_frequency;
-- Top 10 customers by revenue contribution
CREATE VIEW bi_project.top_10_customers_by_revenue AS
SELECT 
    bi_project.customer.customer_name AS customer_name, 
    SUM(bi_project.fact_sales.sales) AS revenue_contribution
FROM 
    bi_project.fact_sales
JOIN 
    bi_project.customer ON bi_project.fact_sales.customer_id = bi_project.customer.customer_id
GROUP BY 
    bi_project.customer.customer_name
ORDER BY 
    revenue_contribution DESC
LIMIT 10;
select * from bi_project.top_10_customers_by_revenue;
-- Most profitable segments
CREATE VIEW bi_project.most_profitable_segments AS
SELECT 
    bi_project.customer.segment AS customer_segment, 
    SUM(bi_project.fact_sales.profit) AS total_profit
FROM 
    bi_project.fact_sales
JOIN 
    bi_project.customer ON bi_project.fact_sales.customer_id = bi_project.customer.customer_id
GROUP BY 
    bi_project.customer.segment
ORDER BY 
    total_profit DESC;
select * from bi_project.most_profitable_segments;
-- Top 5 Most profitable product category
CREATE VIEW bi_project.top_5_profitable_categories AS
SELECT 
    bi_project.product.category AS product_category, 
    SUM(bi_project.fact_sales.profit) AS total_profit
FROM 
    bi_project.fact_sales
JOIN 
    bi_project.product ON bi_project.fact_sales.product_id = bi_project.product.product_id
GROUP BY 
    bi_project.product.category
ORDER BY 
    total_profit DESC
LIMIT 5;
select * from bi_project.top_5_profitable_categories;
-- Top 5 Most profitable products
CREATE VIEW bi_project.top_5_profitable_products AS
SELECT 
    bi_project.product.product_name AS product_name, 
    SUM(bi_project.fact_sales.profit) AS total_profit
FROM 
    bi_project.fact_sales
JOIN 
    bi_project.product ON bi_project.fact_sales.product_id = bi_project.product.product_id
GROUP BY 
    bi_project.product.product_name
ORDER BY 
    total_profit DESC
LIMIT 5;
select * from bi_project.top_5_profitable_products;
-- Effect of higher amounts of discount on sales
CREATE VIEW bi_project.discount_analysis AS
SELECT 
    bi_project.fact_sales.discount AS discount_rate, 
    SUM(bi_project.fact_sales.sales) AS total_sales, 
    SUM(bi_project.fact_sales.profit) AS total_profit
FROM 
    bi_project.fact_sales
GROUP BY 
    bi_project.fact_sales.discount
ORDER BY 
    discount_rate DESC;
select * from bi_project.discount_analysis;
-- Most profitable year
CREATE VIEW bi_project.most_profitable_year AS
SELECT 
    bi_project.date.year AS sales_year, 
    SUM(bi_project.fact_sales.profit) AS total_profit
FROM 
    bi_project.fact_sales
JOIN 
    bi_project.date ON bi_project.fact_sales.order_id = bi_project.date.order_id
GROUP BY 
    bi_project.date.year
ORDER BY 
    total_profit DESC
LIMIT 1;
select * from bi_project.most_profitable_year;
select * from bi_project.fact_sales;






