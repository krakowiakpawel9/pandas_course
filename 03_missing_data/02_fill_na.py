# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd


df = pd.DataFrame(np.random.randn(10, 4),
                  columns=['one', 'two', 'three', 'four'])

# %%
for row in df.values:
    switch = np.random.choice([0, 1])
    if switch:
        i = np.random.choice([0, 1, 2, 3])
        row[i] = np.nan

# %%

df.fillna(0)
df.fillna('No Access')
df['two'] = df['two'].fillna('Special Access Needed')

# %% fill with mean
df = df.fillna(df.mean())

# %%
df = df.fillna(df.median())

# %%
df['one'] = df['one'].fillna(df['one'].mean())
