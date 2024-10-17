import pandas as pd
import pyarrow

# Define the URL
url = "https://drive.google.com/uc?id=1ujY0WCcePdotG2xdbLyeECFW9lCJ4t-K"

pd.set_option('display.max_columns', None)
try:
    # Attempt to read the CSV file
    df = pd.read_csv(url, dtype_backend='pyarrow', on_bad_lines='skip')

    # Print the first 5 rows
    print(df.head())

except Exception as e:
    print(f"An error occurred: {e}")
