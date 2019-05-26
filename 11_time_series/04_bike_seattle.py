# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import wget
import seaborn as sns
import matplotlib.pyplot as plt
sns.set()


# %%
"""
http://data.seattle.gov/
"""
url = ('https://data.seattle.gov/api/views/65db-xm6k/'
      'rows.csv?accessType=DOWNLOAD')

wget.download(url)

# %%

df = pd.read_csv('./bicycle.csv', index_col='Date', parse_dates=True)
df = df.sort_index()

# %%
df.columns = ['East', 'West']
df['Total'] = df.East + df.West

# %%
df.isnull().sum()
df[df['West'].isnull()]
df = df.dropna()

# %%
df.plot(alpha=0.6, color='red')

# %%
df.resample('W').sum().plot(style=[':', '--', '-'])
# %%
df.resample('D').sum().rolling(30).sum().plot(style=[':', '--', '-'])

# %%
hour_gr = df.groupby(df.index.time).mean()
hour_ticks = 4 * 60 * 60 * np.arange(6)
hour_gr.plot(style=[':', '--', '-'], xticks=hour_ticks)

# %%
df['weekend'] = np.where(df.index.weekday < 5, 'Weekday', 'Weekend')

by_weekend_time = df.groupby(['weekend', df.index.time]).mean()

# %%
fig, ax = plt.subplots(1, 2, figsize=(14, 5))
by_weekend_time.loc['Weekday'].plot(ax=ax[0], xticks=hour_ticks)
by_weekend_time.loc['Weekend'].plot(ax=ax[1], xticks=hour_ticks)
