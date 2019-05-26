# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt


# %% loading dataset
path_absolute = ('C:\\Users\\krako\\OneDrive\\Pulpit\\github-repo\\'
                 'pandas_course\\struktury_danych\\01_series\\data\\cdr_d.csv')

path_relative = './dane/cdr_d.csv'

# loading data
df = pd.read_csv(path_absolute)
df = pd.read_csv(path_absolute, sep=',', index_col=0)

# %% preprocessing the data
close_price = df['Zamkniecie']

close_price = close_price['2010-01-01':]

# %% plotting the results - lin scale
close_price.plot(title='Cena akcji spółki CD Projekt')
plt.savefig('./charts/close_lin.png', format='png')

# %% plotting the resutls - log scale
close_price.plot(title='Cena akcji spółki CD Projekt',
                 grid=True,
                 logy=True)
plt.savefig('./charts/close_log.png', format='png')

# %% export data to csv
close_price.to_csv('./data/close_price.csv', header=True)
