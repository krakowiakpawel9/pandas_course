# -*- coding: utf-8 -*-
import pandas as pd


# %% importing dataset
df = pd.read_csv('./data/aapl_us_d.csv', index_col=0)

df.columns = ['Open', 'High', 'Low', 'Close', 'Volume']

# %% slicing data by index
df_2019 = df['2019-01-01':]
df_jan = df['2019-01-01':'2019-02-01']

# %% creating a mask, all DataFrame
df_bool = df_jan > 150
df_jan_150 = df_jan[df_bool]

# %% creating a mask, one column
df_jan['Close'] < 150
df_jan_150 = df_jan[df_jan['Close'] < 150]

# %% query()
df_feb = df['2019-02-01':'2019-03-01']
df_feb.query('Close > 170')

# %% making a flag
df['flag'] = df['Close'] > 200

# removing column
del df['Volume']
