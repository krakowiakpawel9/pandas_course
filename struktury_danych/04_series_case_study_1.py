# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np


# %% loading dataset
path = ('C:\\Users\\krako\\OneDrive\\Pulpit\\github-repo\\pandas_course'
        '\\struktury_danych\\dane\\cdr_d.csv')

# zaladowanie danych
df = pd.read_csv(path)
df = pd.read_csv(path, sep=',', index_col=0)

# %% preprocessing the data
close_price = df['Zamkniecie']

close_price = close_price['2010-01-01':]

# %% plotting the results - lin scale
close_price.plot()

# %% plotting the resutls - log scale
close_price.plot(title='Cena akcji spółki CD Projekt',
                 grid=True,
                 logy=True)

