import requests

url = "https://data.cityofchicago.org/resource/97wa-y6ff.json?$select=driver_type,count(license)&$group=driver_type"

# Make the GET request
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Convert the response to JSON
    records = response.json()
    print(records)  # Output the records
else:
    print(f"Error: {response.status_code} - {response.text}")