# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd


# %% creating dataset
df = pd.DataFrame(np.random.randn(10, 4),
                  columns=['one', 'two', 'three', 'four'])

# %%
for row in df.values:
    switch = np.random.choice([0, 1])
    if switch:
        i = np.random.choice([0, 1, 2, 3])
        row[i] = np.nan

# %%
df.describe()

# %% by row
df.dropna()


# %% by col
df.dropna(axis=1)
