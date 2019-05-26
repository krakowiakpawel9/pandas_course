# -*- coding: utf-8 -*-
import pandas as pd


# %% import data form csv file, comma separated file
df = pd.read_csv('./data/cdr_d.csv', index_col=0)

# select only close price
close_price = df['Zamkniecie']

# export oto csv
close_price.to_csv('./data/close_price.csv', header=['close'])

# export to json
close_price.to_json('./data/close_price.json')

# export to latex
close_price.to_latex('./data/close_price.tex')

# export to python list
close_price_dict = close_price.to_dict()

# %% import data from clipboard
clipboard_df = pd.read_clipboard()

# export to csv file
clipboard_df.to_csv('./data/clipboard.csv', encoding='utf-8')

# export to json file
clipboard_df.to_json('./data/clipboard.json')
