# -*- coding: utf-8 -*-
import pandas as pd


# %% file with only one sheet
df = pd.read_excel('./data/apple.xlsx', index_col=0)

# %% file with more than one sheet
df = pd.read_excel('./data/companies.xlsx', index_col=0, na_values='?')

# %% read second sheet
df_msft = pd.read_excel('./data/companies.xlsx', sheet_name='microsoft')

# %% read google stock price
df_google = pd.read_excel('./data/companies.xlsx', sheet_name='google')
