# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import seaborn as sns
sns.set()


df = pd.read_csv('./data/ten_d.csv', index_col=0)
df.columns = ['Open', 'High', 'Low', 'Close', 'Volume']

# %%
df_agg = df.rolling(window=10).agg(np.mean)

# %%
close_stats = df['Close'].rolling(window=10).agg([np.median, np.mean, np.std])

# %%
df_stats = df.drop('Volume', axis=1)
df_stats = df_stats.rolling(window=10).agg([np.mean, np.std])

# %% different aggregation

diff_agg = df.rolling(window=20).agg({'Close': [np.std, np.mean],
                                      'Volume': np.std})

# %%
df = (df - df.mean()) / df.std()
df = df.rolling(window=30).agg({'Close': np.std, 'Volume': np.std})
df.plot()

# %%
df.rolling(window=len(df), min_periods=1).mean()[:5]