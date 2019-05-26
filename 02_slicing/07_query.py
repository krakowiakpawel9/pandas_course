# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

# %%
np.random.seed(0)
df = pd.DataFrame(np.random.rand(10, 5),
                  columns=list('abcde'))

# %% query
df.query('(a < b)')

df.query('(a < b) & (b < c)')
df.query('(a < b) | (b < c)')

# %%
df = df.round(1)

df.query('c == [0.6, 0.1]')
df.query('c != [0.5]')

df.query('[0.5] in c')
df.query('[0.5, 0.6] not in c')
