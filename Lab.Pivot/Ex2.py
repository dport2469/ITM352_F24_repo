import pandas as pd

# Set display option to show all columns
pd.set_option('display.max_columns', None)

# Define the URL
url = "https://drive.google.com/uc?id=1ujY0WCcePdotG2xdbLyeECFW9lCJ4t-K"

try:
    # Attempt to read the CSV file
    df = pd.read_csv(url, dtype_backend='pyarrow', on_bad_lines='skip')

    # Ensure quantity and unit_price are numeric
    df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')
    df['unit_price'] = pd.to_numeric(df['unit_price'], errors='coerce')

    # Calculate total sales
    df['sales'] = df['quantity'] * df['unit_price']

    # Create a pivot table aggregating sales by sales_region, with columns defined by order_type
    pivot_table = df.pivot_table(
        index='sales_region', 
        columns='order_type', 
        values='sales', 
        aggfunc='sum',
        fill_value=0  # Fill missing values with 0
    )

    # Print the pivot table
    print(pivot_table)

except Exception as e:
    print(f"An error occurred: {e}")
