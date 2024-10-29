import pandas as pd
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

url = "https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value_month=202410"

page_tables = pd.read_html(url)
table = page_tables[0]

for index, row in table.iterrows():
    print(f"Index: {index}, On {row['Date']} the 1 mo intrest rate was {row['1 Mo']}")
