# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd


# %% importing dataset
df = pd.read_csv('./data/aapl_us_d.csv', index_col=0)

df.columns = ['Open', 'High', 'Low', 'Close', 'Volume']

# %% compute new columns
df['average'] = (df['Open'] + df['Close']) / 2

df['daily_change'] = df['Close'] / df['Close'].shift(1) - 1

# %% compute new columns with assign()
df = df.assign(avg=(df['Open'] + df['Close']) / 2)

# %% some exploration
max_daily_change = df['daily_change'].aggregate(max)
min_daily_change = df['daily_change'].aggregate(min)
avg_daily_change = df['daily_change'].aggregate(np.mean)

# %% plot histogram of daily change
df['daily_change'].hist(bins=100, alpha=0.7)

# %% making simple flag
df['flag'] = df['daily_change'] > 0

df['flag'].aggregate(sum)

days_with_positive_return = df['flag'].aggregate(sum) / df['flag'].\
                                       aggregate('count')
