# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np


# %% creating dataset
np.random.seed(0)
df = pd.DataFrame(np.random.randn(20, 5),
                  columns=list('abcde'),
                  index=list('abcdefghijklmnoprstu'))

# %% iloc[row_indexer, column_indexer]
# integer position based

# by col
col_1 = df.iloc[:, 0]
col_2 = df.iloc[:, 1]

col_1_df = df.iloc[:, 0:1]
col_2_df = df.iloc[:, 1:2]

col_1_2 = df.iloc[:, 0:2]
col_1_3 = df.iloc[:, [0, 2]]

col_last = df.iloc[:, -1]
col_last_df = df.iloc[:, -1:]

col_by_2 = df.iloc[:, ::2]

# by row
row_1 = df.iloc[0, :]
row_1_df = df.iloc[0:1, :]

row_1_2 = df.iloc[0:2, :]
row_1_4 = df.iloc[[0, 3], :]

row_last = df.iloc[-1, :]
row_last_df = df.iloc[-1:, :]

row_by_2 = df.iloc[::2, :]
row_by_3 = df.iloc[::3, :]
