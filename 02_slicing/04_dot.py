# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np


# %% creating dataset
np.random.seed(0)
df = pd.DataFrame(np.random.randn(20, 5),
                  columns=list('abcde'),
                  index=list('abcdefghijklmnoprstu'))

# %%

col_a = df.a
col_b = df.b

# %%
mask = df.a > 0
df[mask]

# %%
mask = (df.a > 0) & (df.c > 0)
df[mask]

# %%
mask = df.a > 1
df[mask]

# %%
mask = (df.a > 1) | (df.c > 1)
df[mask]
df[mask][['a', 'c']]

# %% change column
df.e = np.random.randint(0, 10, 20)
