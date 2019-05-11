# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np


# %% generating some random integer values
np.random.seed(0)

A = np.random.randint(0, 10, 10)

series = pd.Series(A, name='random_int')

# %% basic attributes
print(series.dtype)
print(series.iloc[3])
print(series.iloc[-1])
print(series.index)
print(series.is_unique)
print(series.name)
print(series.nbytes)
print(series.shape)

array_A = series.values

# %% generating some random values - normal distribution
np.random.seed(0)
N = np.random.randn(10)
M = np.random.randn(10)

series_N = pd.Series(N, name='normal sample')
series_M = pd.Series(M, name='normal sample')

# %% basic method

# absolute value
series_N.abs()

# adding two Series
series_M.add(series_N)

# subtracting two Series
series_N.subtract(series_M)

# dividing two Series
series_N.divide(series_M)

# compute the dot product
series_N.dot(series_M)

# drop duplicates
series.drop_duplicates()

# drop missing values
series[:3] = np.nan
series.dropna()

# prefix labels
series_N = series_N.add_prefix('dev_')

# sufix labels
series_M = series_M.add_suffix('_data')

# concatenating two Series
concat = series_N.append(series_M)

# idxmax, idxmin
series_N.idxmax()
series_N.idxmin()

# count elements
series_N.count()

# cumulative function
series_N.cummax()
series_N.cummin()
series_N.cumprod()
series_N.cumsum()

# count unique values
series.value_counts()

# sum of values
series_N.sum()

# standard diviation
series_N.std()

# display some basic statistics about dataset
series.describe()

# histogram
hist_data = pd.Series(np.random.randn(10000))
hist_data.hist(bins=80, color='purple')

# top n elements
top_3 = series_N.nlargest(3)

# bottom n elements
bottom_5 = series_N.nsmallest(5)

# quantile
q_1 = series_N.quantile(0.25)
q_2 = series_N.quantile(0.5)
median = series_N.median()
q_3 = series_N.quantile(0.75)

# ranking
rank = series_N.rank()

# round values
round_series = series_N.round(2)

# shifting values
shift_by_1 = series_N.shift(1)
shift_by_2_replace_0 = series_N.shift(2).fillna(0)

# sorting values
sorted_series = series.sort_values()    # ascending
sorted_series_desc = series.sort_values(ascending=False)    # descending
