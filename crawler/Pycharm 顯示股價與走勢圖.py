import requests
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

site = "https://query1.finance.yahoo.com/v8/finance/chart/2330.TW?"
response = requests.get(site)

data = json.loads(response.text)
df = pd.DataFrame(data['chart']['result'][0]['indicators']['quote'][0], index=pd.to_datetime(np.array(data['chart']['result'][0]['timestamp'])*1000*1000*1000))

print(df.head())

df.close.plot()
plt.show()