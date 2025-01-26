import pandas as pd
from google.colab import files

print("Please upload your updated merged file (CSV):")
uploaded_file = files.upload()

filename = list(uploaded_file.keys())[0]
merged_df = pd.read_csv(filename)

merged_df['sales'] = pd.to_numeric(merged_df['sales'], errors='coerce')

top_10_countries = (
    merged_df.groupby("country")["sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

top_10_countries.to_csv("top_10_countries.csv", index=False)

files.download("top_10_countries.csv")

top_10_customers = (
    merged_df.groupby(["customer_id", "customer_name"])
    .agg(
        purchase_frequency=("customer_id", "count"),
        total_sales=("sales", "sum")
    )
    .sort_values(by="total_sales", ascending=False)
    .head(10)
    .reset_index()
)

top_10_customers.to_csv("top_10_customers.csv", index=False)

files.download("top_10_customers.csv")

merged_df['profit'] = pd.to_numeric(merged_df['profit'], errors='coerce')
top_5_profitable_products = (
    merged_df.groupby("product_name")["profit"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
    .reset_index()
)

top_5_profitable_products.to_csv("top_5_profitable_products.csv", index=False)

files.download("top_5_profitable_products.csv")

yearly_profit = (
    merged_df.groupby("year")["profit"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)

yearly_profit.to_csv("yearly_comparisons.csv", index=False)
files.download("yearly_comparisons.csv")

regional_performance_2024 = (
    merged_df[merged_df["year"] == 2024]
    .groupby(["country", "region"])["profit"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)

regional_performance_2024.to_csv("regional_performance_2024.csv", index=False)
files.download("regional_performance_2024.csv")

top_5_profitable_categories = (
    merged_df.groupby("category")["profit"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
    .reset_index()
)

top_5_profitable_categories.to_csv("top_5_profitable_categories.csv", index=False)
files.download("top_5_profitable_categories.csv")

top_5_profitable_segments = (
    merged_df.groupby("segment")["profit"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
    .reset_index()
)

top_5_profitable_segments.to_csv("top_5_profitable_segments.csv", index=False)
files.download("top_5_profitable_segments.csv")

discount_analysis = (
    merged_df[merged_df["year"] == 2024]
    .groupby("discount")
    .agg(
        total_profit=("profit", "sum"),
        total_revenue=("sales", "sum")
    )
    .reset_index()
    .assign(discount=lambda x: pd.to_numeric(x['discount'], errors='coerce'))
    .sort_values(by="discount", ascending=False)
)

discount_analysis.to_csv("discount_analysis.csv", index=False)
files.download("discount_analysis.csv")