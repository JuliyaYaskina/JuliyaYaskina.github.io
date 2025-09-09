import requests
res = requests.get('''
https://search.wb.ru/exactmatch/ru/common/v13/search?ab_testing=false&appType=64&curr=rub&dest=123585762&hide_dtype=13&lang=ru&page=1&query=%D0%B0%D0%BD%D1%82%D0%B8%D1%84%D1%80%D0%B8%D0%B7&resultset=catalog&sort=popular&spp=30&suppressSpellcheck=false
''')
for i, product in enumerate(res.json()['data']['products']):
  print(i, product['name'])
res.json()['data']['products'][0]
""" Результат выполнения 
{'id': 225223196,
 'time1': 3,
 'time2': 34,
 'wh': 507,
 'dtype': 4,
 'dist': 99,
 'root': 202725230,
 'kindId': 0,
 'brand': 'ROLF',
 'brandId': 15879,
 'siteBrandId': 0,
 'colors': [],
 'subjectId': 3935,
 'subjectParentId': 8892,
 'name': 'Антифриз G12+ Red карбоксилатный, красный 5 л',
 'entity': '',
 'matchId': 100896,
 'supplier': 'UPEC DELIVERY официальный магазин Sintec Group',
 'supplierId': 682122,
 'supplierRating': 4.9,
 'supplierFlags': 12227,
 'pics': 4,
 'rating': 5,
 'reviewRating': 4.9,
 'nmReviewRating': 4.9,
 'feedbacks': 275,
 'nmFeedbacks': 275,
 'panelPromoId': 1001424,
 'promoTextCard': 'ОТПУСКАЕМ ЦЕНЫ',
 'promoTextCat': 'ОТПУСКАЕМ ЦЕНЫ',
 'volume': 90,
 'viewFlags': 1318984,
 'sizes': [{'name': '',
   'origName': '0',
   'rank': 0,
   'optionId': 356890038,
   'wh': 507,
   'time1': 3,
   'time2': 34,
   'dtype': 4,
   'price': {'basic': 120800,
    'product': 120800,
    'total': 129800,
    'logistics': 9000,
    'return': 0},
   'saleConditions': 1476395008,
   'payload': 'oddRpEqxRerXaX3X/NgoYOYCRiKgMDo8v3JYYEDjt44by42oMJj4HnbtGHvA6g2X9lRipjtNp/djUAwmMw'}],
 'totalQuantity': 866,
 'log': {'cpm': 1025,
  'promotion': 1,
  'promoPosition': 1,
  'position': 95,
  'advertId': 23690691,
  'tp': 'c'},
 'logs': 'MkFNeTvgmIh3pbBT/krjFyhGhG4Ea3J1ZINkFDwFRbc6dTTowaf03JvOQyYvMl8amKQHckQ/RQ',
 'meta': {'tokens': [], 'presetId': 500050798}}
"""
query = 'антифриз'
max_page = 2
brand = 'SINTEC'
search_arr = []

import datetime
import random

cnt = 0

for page in range(1, max_page + 1):
  print(f'СТРАНИЦА {page}')
  res = requests.get(f'''
    https://search.wb.ru/exactmatch/ru/common/v13/search?ab_testing=false&appType=64&curr=rub&dest=123585762&hide_dtype=13&lang=ru&page={page}&query={query}&resultset=catalog&sort=popular&spp=30&suppressSpellcheck=false
  ''')
  products = res.json()['data']['products']

  for product in products:
    cnt += 1 # cnt = cnt + 1
    if product['brand'] == brand:
      print(product['name'])

      start_date = datetime.datetime(2025, 1, 1)
      finish_date = datetime.datetime(2026, 12, 31)

      diff = (finish_date - start_date).total_seconds()

      random_seconds = random.randint(0, int(diff))

      random_dt = start_date + datetime.timedelta(seconds = random_seconds)

      if product.get('log'):
        search_arr.append([
            product['name'],
            product['log']['cpm'],
            product['log']['position'],
            product['log']['promoPosition'],
            product['log']['tp'],
            query,
            random_dt
        ])
      else:
        search_arr.append([
            product['name'],
            0,
            cnt,
            -1,
            '-',
            query,
            random_dt
        ])

search_arr
""" Результат выполнения
[['Антифриз EURO G11 (-45°С) зеленый, силикатный 5кг',
  1025,
  329,
  11,
  'c',
  'антифриз',
  datetime.datetime(2026, 10, 16, 12, 36, 22)],
 ['Антифриз EURO G11 (-40°С) силикатный, зеленый 5кг',
  1025,
  329,
  13,
  'c',
  'антифриз',
  datetime.datetime(2026, 4, 20, 9, 5, 57)],
 ['Антифриз G11 зеленый',
  255,
  282,
  18,
  'b',
  'антифриз',
  datetime.datetime(2025, 1, 3, 7, 59, 50)],
 ['Антифриз LUXE G12+ (-45°С) карбоксилатный, красный 5кг',
  390,
  319,
  29,
  'c',
  'антифриз',
  datetime.datetime(2025, 1, 27, 20, 13, 18)],
 ['Антифриз готовый фиолетовый Синтек MULTIFREEZE 5кг',
  250,
  315,
  38,
  'b',
  'антифриз',
  datetime.datetime(2025, 12, 11, 8, 25, 31)],
 ['Антифриз G11 зеленый',
  120,
  329,
  61,
  'b',
  'антифриз',
  datetime.datetime(2025, 6, 15, 15, 36, 30)],
 ['Антифриз Antifreeze OEM China OAT red -40 5кг',
  390,
  504,
  65,
  'c',
  'антифриз',
  datetime.datetime(2025, 11, 30, 4, 12, 39)],
 ['Антифриз G11 зеленый',
  135,
  407,
  93,
  'b',
  'антифриз',
  datetime.datetime(2026, 8, 25, 3, 24, 1)],
 ['Антифриз G11 зеленый',
  165,
  464,
  101,
  'b',
  'антифриз',
  datetime.datetime(2025, 4, 9, 12, 23, 49)],
 ['Антифриз G11 зеленый',
  195,
  1052,
  143,
  'b',
  'антифриз',
  datetime.datetime(2025, 2, 6, 3, 29, 13)],
 ['Антифриз Синтек LUXE G12+ (-40) красный 5 кг',
  130,
  813,
  144,
  'b',
  'антифриз',
  datetime.datetime(2025, 5, 9, 2, 16, 53)],
 ['Антифриз G11 зеленый',
  135,
  1052,
  177,
  'b',
  'антифриз',
  datetime.datetime(2025, 6, 24, 11, 4, 46)],
 ['Антифриз Синтек EURO G11 (-40) зеленый 5 кг по цене 4 кг',
  125,
  1177,
  180,
  'b',
  'антифриз',
  datetime.datetime(2026, 9, 6, 13, 34, 38)]]
"""
import pandas as pd

df = pd.DataFrame(search_arr)

df.columns = ['name', 'cpm', 'pos', 'promopos', 'tp', 'query', 'dt']

df['year'] = df['dt'].dt.year

df.groupby(['name', 'query', 'year'])[['pos', 'promopos']].mean()

""" Результат выполнения
			pos	promopos
name	query	year		
Антифриз Antifreeze OEM China OAT red -40 5кг	антифриз	2025	504.0	65.0
Антифриз EURO G11 (-40°С) силикатный, зеленый 5кг	антифриз	2026	329.0	13.0
Антифриз EURO G11 (-45°С) зеленый, силикатный 5кг	антифриз	2026	329.0	11.0
Антифриз G11 зеленый	антифриз	2025	635.8	100.0
2026	407.0	93.0
Антифриз LUXE G12+ (-45°С) карбоксилатный, красный 5кг	антифриз	2025	319.0	29.0
Антифриз Синтек EURO G11 (-40) зеленый 5 кг по цене 4 кг	антифриз	2026	1177.0	180.0
Антифриз Синтек LUXE G12+ (-40) красный 5 кг	антифриз	2025	813.0	144.0
Антифриз готовый фиолетовый Синтек MULTIFREEZE 5кг	антифриз	2025	315.0	38.0
"""
