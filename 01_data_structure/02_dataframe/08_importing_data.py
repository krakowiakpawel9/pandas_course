# -*- coding: utf-8 -*-

"""
@author: krakowiakpawel9@gmail.com
@site: e-smartdata.org
"""

import pandas as pd


# %% importing dataset
df = pd.read_csv('./data/aapl_us_d.csv', index_col=0)

# %% useful method
df.info()
df.describe()

# %% tsv - tab separated file
df = pd.read_csv('./data/aapl_us_d.tsv', sep='\t')
