# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd


ts = pd.Series(np.random.randn(1000),
               index=pd.date_range('2019-01-01', periods=1000))

# %%
ts = ts.cumsum()
ts.plot()

# %%
ts = ts.cummin()
ts.plot()

# %%
ts = ts.cummax()
ts.plot()

# %%
df = pd.DataFrame(np.random.randn(1000, 5),
                  index=pd.date_range('2019-01-01', periods=1000),
                  columns=list('ABCDE'))

# %%
df = df.cumsum()
df.plot()

df['B'].plot()
# %%
df = df.cummin()
df.plot()

# %%
df.iloc[5].plot(kind='bar')
