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

    # Create a pivot table for total sales
    total_sales_pivot = df.pivot_table(
        index='sales_region', 
        columns='order_type', 
        values='sales', 
        aggfunc='sum',
        fill_value=0
    )

    # Create a pivot table for average sales
    avg_sales_pivot = df.pivot_table(
        index='sales_region', 
        columns='order_type', 
        values='sales', 
        aggfunc='mean',
        fill_value=0
    )

    # Combine the two pivot tables
    combined_pivot = pd.concat(
        [total_sales_pivot, avg_sales_pivot],
        axis=1,
        keys=['Total Sales', 'Average Sales']
    )

    # Print the combined pivot table
    print(combined_pivot)

except Exception as e:
    print(f"An error occurred: {e}")
