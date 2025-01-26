from google.colab import files
import pandas as pd

uploaded = files.upload()

file_name = list(uploaded.keys())[0]
merged_df = pd.read_csv(file_name)

print(merged_df.head())

merged_df['order_date'] = pd.to_datetime(merged_df['order_date'], errors='coerce')

merged_df['month'] = merged_df['order_date'].dt.month

merged_df['quarter'] = merged_df['order_date'].dt.to_period('Q').astype(str)

updated_file_path = "updated_merged_file.csv"
merged_df.to_csv(updated_file_path, index=False)

from google.colab import files

files.download(updated_file_path)

product_df = merged_df[['product_id', 'category', 'sub_category', 'product_name']].drop_duplicates()

product_file = 'product_table.csv'
product_df.to_csv(product_file, index=False)
print(f"Product table created and saved as '{product_file}'.")

date_df = merged_df[['order_id', 'order_date', 'ship_date', 'year', 'month', 'quarter']].drop_duplicates()

date_file = 'date_table.csv'
date_df.to_csv(date_file, index=False)
print(f"Date table created and saved as '{date_file}'.")

customer_df = merged_df[['customer_id', 'customer_name', 'segment', 'state', 'country', 'market', 'region', 'order_priority']].drop_duplicates()

customer_file = 'customer_table.csv'
customer_df.to_csv(customer_file, index=False)
print(f"Customer table created and saved as '{customer_file}'.")

sales_df = merged_df[['order_id', 'product_id', 'customer_id', 'sales', 'profit', 'discount', 'quantity', 'shipping_cost']].drop_duplicates()

sales_file = 'sales_table.csv'
sales_df.to_csv(sales_file, index=False)
print(f"Sales table created and saved as '{sales_file}'.")

try:
    from google.colab import files
    files.download(product_file)
    files.download(date_file)
    files.download(customer_file)
    files.download(sales_file)
    print("Files ready for download.")
except ImportError:
    print("If you're not using Google Colab, manually retrieve the CSV files from your working directory.")