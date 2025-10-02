# Sales Data Analysis with ROLAP and Power BI

## Project Overview
This project applies **ROLAP (Relational Online Analytical Processing)** concepts using a **Star Schema** model and **Power BI** for visualization.  
The goal is to analyze sales performance across multiple dimensions such as **countries, customers, products, years, categories, segments, and discounts**.

## Data Source
- Input data provided in **CSV files**.  
- Processed and structured into a **Star Schema**:
  - **Fact Table:** Sales (with measures like revenue, profit, discount, quantity).  
  - **Dimension Tables:** Customers, Products, Dates.  

## Queries & Aggregations
Data was aggregated using SQL queries before visualization. Main analyses include:
- **Top 10 Countries** by sales volume  
- **Top 10 Customers** (purchase frequency, sales, and revenue contribution)  
- **Top 5 Most Profitable Products**  
- **Yearly Comparisons (2021–2024)**: Most profitable year  
- **Regional Performance (2024)**: Most profitable region per country  
- **Top 5 Most Profitable Categories**  
- **Top 5 Most Profitable Segments**  
- **Discount Analysis (2024)**: Impact of discount on profit and revenue  

## Visualizations in Power BI
The following visuals were created:  
- **Pie Chart** → Top Buyers  
- **Pie Chart** → Profit per Category  
- **Pie Chart** → Profit per Segment  
- **Bar Chart** → Top 5 Most Profitable Products  
- **Line Chart** → Discount Effect (on revenue and profit, 2024)  ,Yearly profitability trends 
- **Map** → Sales by Country/Region
  
## Tools & Technologies
- **MySQL** → SQL queries for aggregation  
- **CSV Files** → Intermediate data storage  
- **Power BI** → Visualization & reporting (ROLAP interface)  
- **GitHub** → Project documentation and version control  
