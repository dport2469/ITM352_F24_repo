import json
import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_json('https://drive.google.com/uc?id=1-kvj2Ore88PGzZ9J7_lPBOvNf5C1ohpQ')

# Convert tips to numeric
df['tips'] = pd.to_numeric(df['tips'])

# Group by payment type and sum tips
tips_by_payment = df.groupby('payment_type')['tips'].sum()

plt.bar(list(tips_by_payment.index), tips_by_payment.tolist())
plt.show()
