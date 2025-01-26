import pandas as pd
import json
from google.colab import files

uploaded = files.upload()

csv_file = 'SuperStore_Orders.csv'
csv_data = pd.read_csv(csv_file, encoding='latin-1')

json_file = 'StoreSales.json'
with open(json_file, 'r') as f:
    json_data = json.load(f)

csv_data_split = csv_data.iloc[0, :].str.split(',', expand=True)

num_cols = csv_data_split.shape[1]

if num_cols == 21:
    column_names = [
        'order_id', 'order_date', 'ship_date', 'ship_mode', 'customer_name', 'segment', 'state',
        'country', 'market', 'region', 'product_id', 'category', 'sub_category', 'product_name',
        'sales', 'quantity', 'discount', 'profit', 'shipping_cost', 'order_priority', 'year'
    ][:num_cols]

csv_data_split.columns = column_names

csv_data_split = csv_data_split.iloc[1:]

csv_data_split = pd.read_csv(csv_file, encoding='latin-1', header=0)

csv_data_split['order_date'] = pd.to_datetime(csv_data_split['order_date'], format='%d-%m-%Y', errors='coerce')

csv_data_split['ship_date'] = pd.to_datetime(csv_data_split['ship_date'], format='%d-%m-%Y', errors='coerce')

def update_year(year):
    if year == 2011:
        return 2021
    elif year == 2012:
        return 2022
    elif year == 2013:
        return 2023
    elif year == 2014:
        return 2024
    elif year == 2015:
        return 2025
    else:
        return year

def update_date(date_obj):
    try:
        new_date = date_obj.replace(year=update_year(date_obj.year))
        return new_date
    except ValueError:
        import calendar
        last_day = calendar.monthrange(update_year(date_obj.year), date_obj.month)[1]
        new_date = date_obj.replace(year=update_year(date_obj.year), day=last_day)
        return new_date

csv_data_split['year'] = csv_data_split['year'].apply(update_year)
csv_data_split['order_date'] = csv_data_split['order_date'].apply(update_date)
csv_data_split['ship_date'] = csv_data_split['ship_date'].apply(update_date)
json_df = pd.json_normalize(json_data)
json_df['Order Date'] = pd.to_datetime(json_df['Order Date'], format='%d-%m-%Y')
json_df['Ship Date'] = pd.to_datetime(json_df['Ship Date'], format='%d-%m-%Y')
def update_date_json(date_obj):
    import calendar
    new_year = update_year(date_obj.year)
    last_day_of_month = calendar.monthrange(new_year, date_obj.month)[1]
    new_day = min(date_obj.day, last_day_of_month)
    new_date = date_obj.replace(year=new_year, day=new_day)
    return new_date

json_df['Year'] = json_df['Order Date'].dt.year
json_df['Year'] = json_df['Year'].apply(update_year)
json_df['Order Date'] = json_df['Order Date'].apply(update_date)
json_df['Ship Date'] = json_df['Ship Date'].apply(update_date)
json_df['Order Date'] = json_df['Order Date'].dt.strftime('%Y-%m-%d')
json_df['Ship Date'] = json_df['Ship Date'].dt.strftime('%Y-%m-%d')

csv_data_split.to_csv("modified_data.csv", index=False)

json_df.to_json("modified_data.json", orient="records", indent=4)

print(csv_data_split.head())

"""def update_date(date_obj):
    new_year = update_year(date_obj.year)
    last_day_of_month = calendar.monthrange(new_year, date_obj.month)[1]
    new_day = min(date_obj.day, last_day_of_month)
    new_date = date_obj.replace(year=new_year, day=new_day)  
    return new_date  

json_df['Year'] = json_df['Order Date'].dt.year
json_df['Year'] = json_df['Year'].apply(update_year)
json_df['Order Date'] = json_df['Order Date'].apply(update_date)
json_df['Ship Date'] = json_df['Ship Date'].apply(update_date)
"""

print(json_df.head())

files.download("modified_data.csv")

files.download("modified_data.json")