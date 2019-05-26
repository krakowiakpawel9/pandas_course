# -*- coding: utf-8 -*-
import pandas as pd


# %% importing dataset
df = pd.read_csv('./data/aapl_us_d.csv', index_col=0)

# %% sampling n numbers
sample_10 = df.sample(n=10)

# %% sampling fraction of numbers
sample_10_percent = df.sample(frac=0.1)
