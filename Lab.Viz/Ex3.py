import json
import matplotlib.pyplot as plt
import pandas as pd

pd.set_option('display.max_rows', None)

data_URL = 'https://drive.google.com/uc?id=1-kjcJHN_pCJfB-f3_2xgQNF5U-5PitjU'
df = pd.read_json(data_URL)
# Convert tips to numeric
numbers_cols = ['fare', 'tips']
df[numbers_cols] = df[numbers_cols].astype(float)
# drop missing values from fare and top 
df = df.replace("NaN", pd.NA).dropna(subset=numbers_cols)
# make the scatter plot of fare vs tips
plt.scatter(df['fare'], df['tips'])
plt.title('Tips vs Fares', fontsize=14)
plt.xlabel('Fare', fontsize=12)
plt.ylabel('Tips', fontsize=12)

plt.show()