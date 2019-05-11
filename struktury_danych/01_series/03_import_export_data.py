# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np


# %% import data form csv file, comma separated file
df = pd.read_csv('./dane/cdr_d.csv', index_col=0)

# select only close price
close_price = df['Zamkniecie']

# export oto csv
close_price.to_csv('./dane/close_price.csv', header=['close'])

# export to json
close_price.to_json('./dane/close_price.json')

# export to latex
close_price.to_latex('./dane/close_price.tex')

# export to python list
close_price_list = close_price.to_list()

# export to sql
close_price.to_sql('./dane/close_price.sql')

# %% import data from clipboard
clipboard_df = pd.read_clipboard()

# export to csv file
clipboard_df.to_csv('./dane/clipboard.csv', encoding='utf-8')

# export to json file
clipboard_df.to_json('./dane/clipboard.json')