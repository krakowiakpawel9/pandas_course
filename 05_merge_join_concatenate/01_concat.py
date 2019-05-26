# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd


df1 = pd.DataFrame(np.random.rand(10, 4), columns=list('abcd'))
df2 = pd.DataFrame(np.random.rand(10, 4), columns=list('abcd'))
df3 = pd.DataFrame(np.random.rand(10, 4), columns=list('abcd'))
s = pd.Series(np.random.rand(10), name='x')

# %% concat
df = pd.concat([df1, df2, df3], ignore_index=True)

# %%
df = pd.concat([df1, df2, df3])
df.reset_index()

# %%
df1 = pd.DataFrame(np.random.rand(10, 4), columns=list('abcd'))
df2 = pd.DataFrame(np.random.rand(10, 4), columns=list('efgh'))

df = pd.concat([df1, df2])
df = pd.concat([df1, df2], axis=1)

# %%

df1 = df1[::2]
df = pd.concat([df1,  df2], axis=1, join='outer')
df = pd.concat([df1, df2], axis=1, join='inner')

# %%
# append Series to DataFrame
pd.concat([df1, s])
pd.concat([df1, s], axis=1)

# %%
df1.columns
df2.columns = ['e', 'f', 'g', 'h']
df = pd.concat([df1, df2], axis=1)
