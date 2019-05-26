# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

# %% creating dataset
np.random.seed(0)
df = pd.DataFrame(np.random.randn(31, 5),
                  columns=list('abcde'),
                  index=pd.date_range('20190101', periods=31))

# %% loc method
idx = df.index

day = df.loc['2019-01-01']
day_df = df.loc[:'2019-01-01']

week = df.loc['2019-01-01':'2019-01-07']
after_15 = df.loc['2019-01-15':]
before_15 = df.loc[:'2019-01-15']
