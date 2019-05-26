# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd


index = pd.date_range('01-01-2019', periods=10000)

df = pd.DataFrame(np.random.randn(10000), index=index)

# %% plot cumulating sum
df_cumsum = df.cumsum()
df_cumsum.plot(kind='line')

# %%
df = pd.DataFrame(np.random.rand(100), index=index)
df.plot(kind='line')
