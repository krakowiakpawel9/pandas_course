# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np


# %% generating sample normal distribution
np.random.seed(0)

A = np.random.randn(20)

s = pd.Series(A, name='los')

# %% aggregate - very useful
count = len(s)
minimum = s.aggregate(min)
maximum = s.aggregate(max)
suma = s.aggregate(sum)
mean = s.aggregate(np.mean)
std = s.aggregate(np.std)

# %% multiple aggregation
stats = s.aggregate(['min', 'max', 'sum', 'mean'])

stats_np = s.aggregate([np.prod, np.mean, np.sum, np.std, np.median])