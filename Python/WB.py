import requests
from datetime import datetime

arr = []

page = 1
query = 'лонгслив женский оверсайз'

res = requests.get(
    f"https://search.wb.ru/exactmatch/ru/female/v9/search?ab_testing=false&appType=64&curr=rub&dest=123585762&hide_dtype=13&lang=ru&page={page}&query={query}&resultset=catalog&sort=popular"
)

query_list = [
    'лонгслив женский оверсайз',
    'лонгслив женский'
]

max_page = 3
brand = 'ТЕЛОДВИЖЕНИЯ'

for query in query_list:
  for page in range(1, max_page + 1):
    res = requests.get(
      f"https://search.wb.ru/exactmatch/ru/female/v9/search?ab_testing=false&appType=64&curr=rub&dest=123585762&hide_dtype=13&lang=ru&page={page}&query={query}&resultset=catalog&sort=popular"
    )
    for card in res.json()['data']['products']:
      if card.get('log') and card['brand'] == brand:
        arr.append([
            card['log']['position'],
            card['log']['promoPosition'],
            datetime.now(),
            query,
            card['name']
        ])
    # print(f"query: {query}, page: {page}")

import pandas as pd

df = pd.DataFrame(arr)

df.columns = ['position', 'promo_position', 'created_at', 'query', 'name']

df
	
df['diff'] = df['position'] - df['promo_position']

df1

df1 = df[df['name'] == 'Лонгслив женский оверсайз с принтом FOREVER YOUNG']

import matplotlib.pyplot as plt

plt.plot(df1['position']);


df1 = df[df['name'] == 'Лонгслив женский оверсайз с принтом FOREVER YOUNG']

pd.pivot_table(
    df1,
    index='query',
    columns='hour',
    values='promo_position',
    aggfunc='mean'
)

df['hour'] = df['created_at'].dt.hour
df['date'] = df['created_at'].dt.date

df

import plotly.express as px

px.line(df1['position'])

res.json()['data']['products'][1]
