import json
import matplotlib.pyplot as plt
import pandas as pd

pd.set_option('display.max_rows', None)
df = pd.read_json('https://drive.google.com/uc?id=1-kvj2Ore88PGzZ9J7_lPBOvNf5C1ohpQ')

# Convert tips to numeric

df =  df.replace("NaN", pd.NA).dropna()

numbers_cols = ['fare', 'tips']
df[numbers_cols] = df[numbers_cols].astype(float)

# Group by payment type and sum tips
tips_by_payment = df.groupby('payment_type')['tips'].sum()

plt.bar(list(tips_by_payment.index), tips_by_payment.tolist())
plt.title('Total tips by Payment Method', fontsize=14)
plt.xlabel('Payment Method', fontsize=12)
plt.ylabel('Total Tips', fontsize=12)
plt.show()
