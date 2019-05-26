# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('./data/ten_d.csv', index_col=0)
df.columns = ['Open', 'High', 'Low', 'Close', 'Volume']
clean_price = df[['Open', 'High', 'Low', 'Close']]

# %%
corr_matrix = clean_price.corr().round(2)

# %% corr beteen Series
df['Open'].corr(df['Close'])

# %% plot correlation matrix
plt.matshow(clean_price.corr())

# %% using seaborn
sns.heatmap(corr_matrix,
            xticklabels=corr_matrix.columns.values,
            yticklabels=corr_matrix.columns.values)
