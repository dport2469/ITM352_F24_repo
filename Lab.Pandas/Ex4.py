import pandas as pd

# Load the JSON file into a DataFrame
df = pd.read_json('./Taxi_Trips.json')

# Print summary statistics
summary_statistics = df.describe()
print("Summary Statistics:")
print(summary_statistics)

# Print the median
median_values = df["fare"].median()
print("\nMedian Values:")
print(median_values)