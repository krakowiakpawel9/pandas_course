# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

np.random.seed(0)

df_1 = pd.DataFrame(np.random.randn(10, 3), columns=list('abc'))
df_2 = pd.DataFrame(np.random.randn(10, 3), columns=list('abc'))

# %% basic arithmetic
df_1 + df_2
df_1 - df_2
df_1 * df_2
df_1 / df_2

df_1 ** 2

# %% slicing
df_1 > 0
df_1[df_1 > 0]

df_1['b'] > 0
df_1[df_1['b'] > 0]

np.exp(df_1)
df_1.T
