import json
import matplotlib.pyplot as plt
import pandas as pd

pd.set_option('display.max_rows', None)

data_URL = 'https://drive.google.com/uc?id=1-kvj2Ore88PGzZ9J7_lPBOvNf5C1ohpQ'
df = pd.read_json(data_URL)
# Convert tips to numeric
numbers_cols = ['fare', 'tips', 'trip_miles']
df[numbers_cols] = df[numbers_cols].astype(float)
# drop missing values from fare and top 
df = df.replace("NaN", pd.NA).dropna(subset=numbers_cols)
# make the scatter plot of fare vs tips
plt.plot(df['fare'], df['trip_miles'], linestyle= "none",         
            marker='v',     # Triangle down marker
            c='cyan',       # Cyan color
            alpha=0.2      # 20% opacity
            )
plt.title('Trip Miles vs Fares', fontsize=14)
plt.xlabel('Fare', fontsize=12)
plt.ylabel('Trip Miles', fontsize=12)

plt.show()