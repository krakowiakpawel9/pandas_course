# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd


df = pd.DataFrame(np.random.randn(10, 4),
                  columns=['one', 'two', 'three', 'four'])

# %% simple
for row in df.values:
    i = np.random.choice([0, 1, 2, 3])
    row[i] = np.nan

# %%
for row in df.values:
    switch = np.random.choice([0 ,1])
    if switch:
        i = np.random.choice([0, 1, 2, 3])
        row[i] = np.nan


# %%  isnull()
df.isnull()
df['one'].isnull()

# %%
df[df['one'].isnull()]

# %%
df[~df['one'].isnull()]

# %% notnull()
df.notnull()

df[df.notnull()]

df[df['two'].notnull()]
df[~df['two'].notnull()]

# add column with nan
df['five'] = np.nan

# delete column
del df['five']

df.drop('five', axis=1)
# %% calculations with missing data

# when summing NaN is treated as zero
df['one'].sum()

# cumulative method ignore NaN
df['one'].cumsum()
df['one'].cumsum(skipna=False)

# %%
df.mean()   # by row
df.mean(axis=1)    # by col
df.count()

# %% NaN are excluded
df.groupby('one').mean()
