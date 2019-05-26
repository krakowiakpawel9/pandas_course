# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np


# %%
np.random.seed(0)
df = pd.DataFrame(np.random.randn(20, 5),
                  columns=list('abcde'),
                  index=list('abcdefghijklmnoprstu'))

# %% loc[row_indexer, column_indexer]
# key notes:
#     label based
#     slice 'a':'f' both the start and stop are included

# by col
col_a = df.loc[:, 'a']
col_b = df.loc[:, 'b']
col_a_b = df.loc[:, ['a', 'b']]
col_a_c = df.loc[:, ['a', 'c']]
col_b_c_d = df.loc[:, 'b':'d']

# by row
row_a = df.loc['a', :]
row_a_b = df.loc[['a', 'b'], :]
row_a_u = df.loc[['a', 'u'], :]
row_b_e_g = df.loc[['b', 'e', 'g'], :]

# %% by row and col
row_a_col_a = df.loc['a', 'a']
row_a_d_col_a = df.loc[['a', 'd'], 'a']
row_a_u_col_a_e = df.loc[['a', 'u'], ['a', 'e']]
