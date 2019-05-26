# -*- coding: utf-8 -*-
import pandas as pd
import seaborn as sns
sns.set()


"""
count() - number of non-null observations
sum()
mean()
median()
min()
max()
std()
var() - unbiased variance
skew() - skewness - 3 moment
kurt() - kurtosis - 4 moment
quantile()
apply()
cov()
corr()
"""

df = pd.read_csv('./data/ten_d.csv', index_col=0)
df.columns = ['Open', 'High', 'Low', 'Close', 'Volume']
clean_price = df[['Open', 'High', 'Low', 'Close']]

# %% Series
vol = df['Volume']
cum_vol = vol.cumsum()

# %%
cum_vol.plot()

# %%
close = df['Close']
close_rol = close.rolling(window=30).mean()
close.plot()
close_rol.plot(style='k--')

# %% rolling means
close.plot(color='black')
for i in [5, 10, 15, 20, 60]:
    close_rol = close.rolling(window=i).mean()
    close_rol.plot()

# %% simple strategy
close.plot(color='black')
for i in [5]:
    close_rol_min = close.rolling(window=i).min()
    close_rol_min.plot()
    close_rol_max = close.rolling(window=i).max()
    close_rol_max.plot()

# %% DataFrame
clean_price.rolling(window=20).mean().plot()
close.plot()

# %% DataFrame, std
close.rolling(window=15).std().plot()
close.plot()

# %% DataFreame subplots
clean_price.rolling(window=20).mean().plot(subplots=True)

# %% apply, custom indicator
aa = close.rolling(window=10).apply(lambda x: abs(x - x.mean()).mean())
aa.plot()