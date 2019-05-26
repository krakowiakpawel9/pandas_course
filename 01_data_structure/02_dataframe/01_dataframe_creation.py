# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd


# %% creating first DataFrame 2x3

df = pd.DataFrame(data=[12, 14, 16], index=['first', 'second', 'third'],
                  columns=['col_1'])

df = pd.DataFrame(data=[[12, 14, 16], [45, 23, 12]], index=['first', 'second'],
                  columns=['col_1', 'col_2', 'col_3'])

# %% 3x3
df = pd.DataFrame(data=[[1, 2, 3],
                        [5, 6, 6],
                        [7, 8, 9]], index=['a', 'b', 'c'],
                  columns=['col_a', 'col_b', 'col_c'])

# %% creating DataFrame from dict of Series

d = {'one': pd.Series([1, 2, 3]),
     'two': pd.Series([4, 5, 6])}
df = pd.DataFrame(d)

# %% creating DataFrame from dict of Series

d = {'one': pd.Series([1, 2, 3]),
     'two': pd.Series([4, 5, 6]),
     'flag': ['yes', 'no', 'no']}
df = pd.DataFrame(d)

# %% creating DataFrame from dict of Series diffrent size
d = {'one': pd.Series([1, 2, 3]),
     'two': pd.Series([4, 5, 6, 7])}
df = pd.DataFrame(d)

# %% creating DataFrame from dict of Series with numpy
d = {'one': pd.Series(np.random.randn(100)),
     'two': pd.Series(np.random.randn(100)),
     'three': pd.Series(np.random.randn(100))}
df = pd.DataFrame(d)

# %% getting index and columns
df.index
df.columns

# %% creating DataFrame from a list of dictionaries
list_of_dicts = [{'apple': 1, 'orange': 4},
                 {'apple': 2, 'orange': 3, 'mango': 2}]

df = pd.DataFrame(list_of_dicts)

for col in df.columns:
    print(col)

big_letters = [col.upper() for col in df.columns]
df.columns = big_letters

# %% creating DataFrame form a dictionary
d = {'wig20': ['PKN Orlen', 'PKO BP', 'LPP'],
     'mWig40': ['Amica', 'Playway', 'Benefit']}

df = pd.DataFrame(d)
