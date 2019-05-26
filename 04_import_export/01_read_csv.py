# -*- coding: utf-8 -*-
import pandas as pd


# %% basic import
df = pd.read_csv('./data/apple.csv')

# %% import with index_col argument
df = pd.read_csv('./data/apple.csv', index_col=0)

# %% import, skip first n rows
df_skip = pd.read_csv('./data/apple.csv', index_col=0, sep=',', skiprows=5)

# %% import, read only first n rows, useful with larger datasets
df_nrows = pd.read_csv('./data/apple.csv', index_col=0, sep=',', nrows=100)

# %% read reviews
df = pd.read_csv('./data/reviews_clean.csv')
