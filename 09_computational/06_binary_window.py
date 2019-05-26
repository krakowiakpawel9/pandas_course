# -*- coding: utf-8 -*-
import pandas as pd
import seaborn as sns
sns.set()

df = pd.read_csv('./data/ten_d.csv', index_col=0)
df.columns = ['Open', 'High', 'Low', 'Close', 'Volume']

# %%
open_price = df['Open']
close_price = df['Close']
df['Daily_Change'] = df['Close'].pct_change()
corr = df.corr()

# %%
rolling_corr = open_price.rolling(window=60).corr(close_price)
rolling_corr.plot()

# %%
df_roll = df.rolling(window=20).corr(df['Close']).drop('Close', axis=1)
df_roll.plot()