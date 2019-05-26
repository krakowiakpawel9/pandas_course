# -*- coding: utf-8 -*-
import pandas as pd


# %% importing dataset
df = pd.read_csv('./data/aapl_us_d.csv', index_col=0)

# %% select only n first row
df.iloc[:10]
df.iloc[0]
df.iloc[0:1]
df.iloc[-1]
df.iloc[::2]
df.iloc[::30]

df.iloc[:5]
df.iloc[:5, 0:4]
df.iloc[5:10, 0:2]
df.iloc[5:10, [0, 2]]
df.iloc[[0, -1]]

