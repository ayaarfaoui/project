import pandas as pd
from google.colab import files

uploaded = files.upload()

csv_file = list(uploaded.keys())[0]
json_file = list(uploaded.keys())[1]

csv_df = pd.read_csv(csv_file)
json_df = pd.read_json(json_file)

import uuid

csv_df["customer_id"] = [f"csv_{uuid.uuid4().hex[:8]}" for _ in range(len(csv_df))]

csv_df.columns = csv_df.columns.str.lower()
json_df.columns = json_df.columns.str.lower()

json_df.columns = json_df.columns.str.replace(' ', '_').str.lower()
csv_df.columns = csv_df.columns.str.replace(' ', '_').str.lower()

json_df = json_df.drop(columns=["row id", "city", "postal code"], errors='ignore')

json_df['year'] = json_df['year'].fillna(json_df['year'].mode()[0])  # You can replace with 0 if preferred
csv_df['year'] = csv_df['year'].fillna(csv_df['year'].mode()[0])

json_df['year'] = json_df['year'].astype(int)
csv_df['year'] = csv_df['year'].astype(int)

print(csv_df.head())

print(json_df.head())

csv_df = csv_df.drop_duplicates()
json_df = json_df.drop_duplicates()

csv_df = csv_df.fillna("Unknown")
json_df = json_df.fillna("Unknown")

column_order = [
    'order_id', 'order_date', 'ship_date', 'ship_mode', 'customer_id', 'customer_name',
    'segment', 'state', 'country', 'market', 'region', 'product_id', 'category',
    'sub_category', 'product_name', 'sales', 'quantity', 'discount', 'profit',
    'shipping_cost', 'order_priority', 'year'
]

for col in column_order:
    if col not in csv_df.columns:
        csv_df[col] = pd.NA
    if col not in json_df.columns:
        json_df[col] = pd.NA

csv_df = csv_df[column_order]
json_df = json_df[column_order]

csv_cleaned_file = "cleaned_csv_file.csv"
json_cleaned_file = "cleaned_json_file.json"

csv_df.to_csv(csv_cleaned_file, index=False)
json_df.to_json(json_cleaned_file, orient="records", lines=True)

from google.colab import files

files.download(csv_cleaned_file)

files.download(json_cleaned_file)

merged_df = pd.concat([csv_df, json_df], ignore_index=True)

merged_df = merged_df.drop_duplicates()

merged_file = "merged_data_file.csv"
merged_df.to_csv(merged_file, index=False)

print("Downloading merged data file...")
files.download(merged_file)