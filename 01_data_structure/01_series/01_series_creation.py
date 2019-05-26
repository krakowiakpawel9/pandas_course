# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np


# %% Example 1 - scalar
s = pd.Series(3)

# %% Example 2 - creating Series by definition
s_def = pd.Series(data=[21, 34, 52, 56, 67],
                  index=['pawel', 'tomek', 'adam', 'kuba', 'jan'],
                  dtype='float32',
                  name='age')

# %% Example 3 - creating Series from numpy array
A = np.random.randn(5)
s = pd.Series(data=A, index=['a', 'b', 'c', 'd', 'e'])

print(s)
print(s.index)

s = pd.Series(A)

# %% Example 4 - creating Series from python dictionary, text values
stocks = {'Apple': 'USA', 'CD Projekt': 'Poland', 'Amazon': 'USA'}
stocks_series = pd.Series(stocks, name='stock')

# %% Example 5 - creating Series from python dictionary, text values
stocks_price = {'Apple': 196, 'CD Projet': 212, 'Amazon': 1877}
stocks_price_series = pd.Series(stocks_price)

# %% Example 6 - convert Series to numpy array
stocks_price_array = stocks_price_series.values

# %% Example 7 - slicing
apple_price = stocks_price['Apple']
print('Cena akcji Apple wynosi {}.'.format(apple_price))

# %% Example 8 - more slicing
np.random.seed(0)

A = np.random.randn(20)
s = pd.Series(A)

s[0]
s[1]
s[5:10]
s[:10]
s[5:]
s[::2]
s[::3]

# %% Example 9 - checking memberdhip
stocks_price = {'Apple': 196, 'CD Projet': 212, 'Amazon': 1877}
stocks_price_series = pd.Series(stocks_price)

'Apple' in stocks_price
'Google' in stocks_price
'Google' not in stocks_price
