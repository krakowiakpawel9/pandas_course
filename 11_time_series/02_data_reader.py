# -*- coding: utf-8 -*-
import pandas as pd
from pandas_datareader.data import DataReader
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


# %%
amazon = DataReader('AMZN', 'stooq')
amazon.to_csv('data.csv')

# %%
amazon['Close'].plot()
amazon['Close'].plot(alpha=0.5)

# %%
amazon['Close'].plot(alpha=0.7)
amazon.resample('BQ').mean()['Close'].\
       plot(color='green', style='--', alpha=0.7)

plt.legend(['price', 'quarter average'])

# %% shifting
fig, ax = plt.subplots(3, sharex=True)

amazon['Close'].plot(ax=ax[0])
amazon['Close'].shift(365).plot(ax=ax[1])
amazon['Close'].shift(-365).plot(ax=ax[2])

ax[0].legend(['input'])
ax[1].legend(['shift by 365'])
ax[2].legend(['shift by -365'])

# %% ROI
ROI = 100 * (amazon.shift(16) / amazon - 1)
ROI['Close'].plot()

# %% rolling windows
amazon = amazon.sort_index()
rolling = amazon['Close'].rolling(120)
df = pd.DataFrame({'input': amazon['Close'],
                   'rolling_mean': rolling.mean(),
                   'rolling_std': rolling.std()})

fig, ax = plt.subplots(2, sharex=True)
amazon['Close'].plot(ax=ax[0])
amazon['Close'].rolling(120).mean().plot(ax=ax[0], logy=True)
amazon['Close'].rolling(120).std().plot(ax=ax[1], logy=True)

ax[0].legend(['price', 'rolling_mean'])
ax[1].legend(['rolling_std'])
