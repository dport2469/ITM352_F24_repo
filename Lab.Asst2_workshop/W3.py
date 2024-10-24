import pandas as pd
import pyarrow # not needed, but it's a good practice to import it
import time

# The file at this URL contains a large data set. It must be downloadable and in CSV format to be read by pandas.
url = "https://drive.google.com/uc?id=1ujY0WCcePdotG2xdbLyeECFW9lCJ4t-K"
test_data_file = "sales_data_test.csv"

# Set display option to show all columns
pd.set_option('display.max_columns', None)

def load_csv(data_file_path):
    try:
        # Attempt to read the CSV file
        print(f"Reading CSV file...")
        time_start = time.time()
        sales_data = pd.read_csv(data_file_path, dtype_backend='pyarrow', on_bad_lines='skip')
        print(f"Sales data loaded in { (time.time() - time_start)} seconds")
        print(f"There are {len(sales_data)} rows with columns {sales_data.columns}")


        # replace missing data with 0's
        sales_data.fillna(0, inplace=True)

        # We ask Pandas to parse the order_date field to turn it into a standard representation.
        sales_data['order_date'] = pd.to_datetime(sales_data['order_date'], format='mixed')

    except Exception as e:
        print(f"An error occurred: {e}")

    columns_to_check = ["quantity", "unit_price"]

    # Check if all specified columns are in the DataFrame
    all_required_present = all(col in sales_data.columns for col in columns_to_check)

    if all_required_present:
        print("All specified columns are present in the DataFrame.")
    else:
        print("Some specified columns are missing from the DataFrame.")
    return sales_data


# this function will diaplay # rows of sales data requested by the user
def display_initial_rows(data):
    total_rows = len(data)
    user_input = input(f"How many initial rows would you like to see? (Enter a number up to {total_rows}, 'all', or leave empty to skip): ")
    if user_input.lower() == "all":
        print(data)  # Display all rows
    elif user_input.strip() == "":
        print("Skipping preview.")
    else:
        try:
            num_rows = int(user_input)
            if num_rows < 0:
                print("Please enter a non-negative number.")
            elif num_rows > total_rows:
                print(f"Please enter a number up to {total_rows}.")
            else:
                print(data.head(num_rows))  # Display the specified number of rows
                
        except ValueError:
            print("Invalid input. Please enter a valid number, 'all', or leave empty to skip.")


# main
sales_data = load_csv(test_data_file)
# main loop
def main():
    while(True):
        display_initial_rows(sales_data)

if  (__name__ == "__main__"):
    main()