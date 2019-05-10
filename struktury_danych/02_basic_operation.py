# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np


# %% generating some random integer values
np.random.seed(0)

A = np.random.randint(0, 10, 10)
B = np.random.randint(0, 10, 10)

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

# aggregate values - very useful
suma = series_N.aggregate(sum)
minimum = series_N.aggregate(min)
maximum = series_N.aggregate(max)
squared_values = series_N.aggregate(lambda x: x**2)
mean = series_N.aggregate(np.mean)
std = series_N.aggregate(np.std)

# concatenating two Series
concat = series_N.append(series_M)

# applying functions to Series
series_N.apply(lambda x: 100 * x)

def custom_function(x):
    return 10 * x

series_N.apply(custom_function)

# idxmax, idxmin
series_N.idxmax()
series_N.idxmin()

series_N.count()

# cumulative function
series_N.cummax()
series_N.cummin()
series_N.cumprod()
series_N.cumsum()

# display some basic statistics about dataset
series.describe()

# histogram
hist_data = pd.Series(np.random.randn(10000))
hist_data.hist(bins=80)













