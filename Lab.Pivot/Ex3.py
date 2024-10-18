import pandas as pd
import pyarrow # not needed, but it's a good practice to import it
import numpy as np # numpy has more efficient functions for numerical operations especially for large datasets

# The file at this URL contains a large data set. It must be downloadable and in CSV format to be read by pandas.
url = "https://drive.google.com/uc?id=1ujY0WCcePdotG2xdbLyeECFW9lCJ4t-K"

# Set display option to show all columns
pd.set_option('display.max_columns', None)
# Set output format for float values to 2 decimal places
pd.set_option("display.float_format", "${:,.2f}".format)

try:
    # Attempt to read the CSV file
    sales_data = pd.read_csv(url, dtype_backend='pyarrow', on_bad_lines='skip')

    # We ask Pandas to parse the order_date field to turn it into a standard representation.
    sales_data['order_date'] = pd.to_datetime(sales_data['order_date'], format='mixed')

    # Print the first 5 rows
    print(sales_data.head())

    # Ensure quantity and unit_price are numeric
    sales_data['quantity'] = pd.to_numeric(sales_data['quantity'], errors='coerce')
    sales_data['unit_price'] = pd.to_numeric(sales_data['unit_price'], errors='coerce')

    # Calculate total sales
    sales_data['sales'] = sales_data['quantity'] * sales_data['unit_price']

    # Create a pivot table aggregating sales by sales_region, with columns defined by order_type
    sales_pivot = sales_data.pivot_table(
        index='sales_region', 
        columns='order_type', 
        values='sales', 
        aggfunc=[np.sum, np.mean],
        fill_value=0  # Fill missing values with 0
    )

    print(sales_pivot)

except Exception as e:
    print(f"An error occurred: {e}")