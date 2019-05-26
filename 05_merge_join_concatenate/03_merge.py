# -*- coding: utf-8 -*-
import pandas as pd


ten_pl = pd.read_csv('./data/ten.csv', index_col=0)
plw_pl = pd.read_csv('./data/plw.csv', index_col=0)

# ten = ten_pl
# plw = plw_pl

ten = ten_pl.copy()
plw = plw_pl.copy()

ten.columns = ['Open', 'High', 'Low', 'Close', 'Volume']
plw.columns = ['Open', 'High', 'Low', 'Close', 'Volume']

# %% merge on index, inner
df = pd.merge(ten, plw, how='inner', left_index=True, right_index=True)

# %%
df = pd.merge(ten, plw, how='inner', left_index=True, right_index=True,
              suffixes=('_TEN', '_PLW'))

# %% merge on index, outer
df = pd.merge(ten, plw, how='outer', left_index=True, right_index=True)

# %%
df = pd.merge(ten, plw, how='outer', left_index=True, right_index=True,
              suffixes=('_TEN', '_PLW'))

# %% generate daily changes
ten['Change'] = ten['Close'] / ten['Close'].shift() - 1
plw['Change'] = plw['Close'] / plw['Close'].shift() - 1

# %% generate flag 1 if change > 0, 0 if change < 0
ten['Flag'] = ten['Change'] > 0
plw['Flag'] = plw['Change'] > 0

ten['Flag'] = ten['Flag'].apply(int)
plw['Flag'] = plw['Flag'].apply(int)

# %% merge table
df = pd.merge(ten, plw, how='inner', left_index=True, right_index=True,
              suffixes=('_TEN', '_PLW'))

correlation_matrix = df.corr()

# %% select where Flag_TEN = Flag_PLW = 1
df_positive = df[(df['Flag_TEN'] == 1) & (df['Flag_PLW'] == 1)]

df_positive_2 = df.query('(Flag_TEN == 1) & (Flag_PLW == 1)')
