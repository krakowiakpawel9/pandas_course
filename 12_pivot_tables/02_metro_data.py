# -*- coding: utf-8 -*-
import pandas as pd
import seaborn as sns
sns.set()


url = ('https://archive.ics.uci.edu/ml/machine-learning-databases/00492/'
       'Metro_Interstate_Traffic_Volume.csv.gz')

# %%
metro = pd.read_csv(url, compression='gzip', parse_dates=True,
                    index_col='date_time')

metro = metro.loc['2016-01-01':]

# %%
traffic = metro.iloc[:, -1:]
traffic.plot()
tr = traffic.resample('M').sum()
tr.plot()

# %%
metro.pivot_table(values='traffic_volume', index='weather_main').\
      plot(kind='bar')

metro.groupby('holiday').mean()['traffic_volume'].plot(kind='bar')
