# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd


# creating a Series
list_of_wig20_stocks = ['Alior', 'CCC', 'CD Projekt', 'Cyfrowy Polsat', 'Dino',
                        'JSW', 'KGHM', 'Lotos', 'LPP', 'mBank', 'Orange',
                        'PEKAO SA', 'PGE', 'PGNIG', 'PKN ORLEN', 'PKO BP',
                        'PLAY', 'PZU', 'Santander', 'Tauron']

wig20 = pd.Series(list_of_wig20_stocks, name='WIG 20')

# standardization of names
wig20 = wig20.apply(lambda word: word.upper())

# %% checking if company is in WIG20
print(wig20.isin(['CCC']))

wig20[wig20.isin(['DINO', 'LPP'])]

# %% Series is iterable
for company in wig20:
    print(company)


for company in wig20:
    company = company + '_PLN'
    print(company)

stocks_with_len_4 = []
for company in wig20:
    if len(company) == 4:
        stocks_with_len_4.append(company)
print(stocks_with_len_4)

# list comprehension
stocks_wit_len_5 = [company for company in wig20 if len(company) == 5]
