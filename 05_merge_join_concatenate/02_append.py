# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd


df1 = pd.DataFrame(np.random.rand(10, 4), columns=list('abcd'))
df2 = pd.DataFrame(np.random.rand(10, 4), columns=list('abcd'))
df3 = pd.DataFrame(np.random.rand(10, 4), columns=list('abcd'))

# %%
df = df1.append(df2).sort_index().reset_index()
del df['index']

# %%
df = df1.append(df2).sort_index().reset_index().drop('index', axis=1)

# %%
df = df1.append(df2, ignore_index=True)