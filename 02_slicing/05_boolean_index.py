# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

# %% creating dataset
np.random.seed(0)
df = pd.DataFrame(np.random.randn(31, 5),
                  columns=list('abcde'),
                  index=pd.date_range('20190101', periods=31))

# %%
mask = df > 0
df_gt_0 = df[mask]

df_gt_0 = df[df > 0]

# %%
df[df < -1]
df[(df < -1) | (df > 1)]
df[(df > 0.5) & (df < 1.)]

df[df < 0]
df[~(df < 0)]

df[(df < 0) & ~(df < 0)]
df[(df < 0) | ~(df < 0)]

# %%
