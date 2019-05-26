# -*- coding: utf-8 -*-
import pandas as pd


# %% read from html file
df = pd.read_html('./data/small.html', header=0, index_col=0)[0]

# %% read from website
df = pd.read_html('https://www.biznesradar.pl/gielda/indeks:WIG20',
                  header=0, index_col=0)

# %% read from website
df = pd.read_html('https://stooq.pl/t/?i=510',
                  header=0, index_col=0)

# %% read from website
df = pd.read_html('https://finance.yahoo.com/cryptocurrencies',
                  header=0, index_col=0)
