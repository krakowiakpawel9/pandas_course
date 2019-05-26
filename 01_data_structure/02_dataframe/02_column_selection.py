# -*- coding: utf-8 -*-
import pandas as pd


# %% importing dataset
df = pd.read_csv('./data/aapl_us_d.csv', index_col=0)

# %% change column names
print(df.columns)
english_name = ['Open', 'High', 'Low', 'Close', 'Volume']

df.columns = english_name

# %% select one column
open_price = df['Open']
open_price = df.iloc[:, 0]
high_price = df.iloc[:, 1]

close_price = df.Close
volume = df.Volume

last_column = df.iloc[:, -1]
# last_column = df[-1] error

# %% select two or more columns
two = df[['Open', 'Close']]
three = df.iloc[:, [0, 3]]

from_open_to_close = df.iloc[:, 0:4]
from_open_to_close = df.iloc[:, :-1]
