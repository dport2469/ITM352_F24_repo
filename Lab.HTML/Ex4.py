from sodapy import Socrata
import pandas as pd

# Initialize Socrata client
client = Socrata("data.cityofchicago.org", None)

# Fetch the first 500 records from the dataset
results = client.get("rr23-ymwb", limit=500)

# Convert to pandas DataFrame
df = pd.DataFrame.from_records(results)
columns = ['vehicle_type', 'vehicle_fuel_source']
print(df.groupby('vehicle_fuel_source').size().reset_index(name='number_of_vehicles'))