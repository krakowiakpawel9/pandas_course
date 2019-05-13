# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

# %%
s = pd.Series(np.random.randn(20))

np.random.seed(0)
df = pd.DataFrame(np.random.randn(31, 2),
                  columns=list('ab'),
                  index=pd.date_range('20190101', periods=31))

# %% Series
s[s > 0]
s.where(s > 0)

# %% DataFrame
df[df > 0]
df.where(df > 0)

df.where(df > 0, 0)
from_0_to_1 = df.where(df > 0, 0).where(df < 1, 1)

# %%
df.where(df > 0, inplace=True)

# %%
df.where(df.a > 0)
