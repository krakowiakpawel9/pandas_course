# -*- coding: utf-8 -*-
import pandas as pd
import seaborn as sns
sns.set()


# %%
df = pd.read_csv('./data/ten_d.csv', index_col=0)
df.columns = ['Open', 'High', 'Low', 'Close', 'Volume']
clean_price = df[['Open', 'High', 'Low', 'Close']]

# %%
volume = df[['Volume']].copy()
volume['Volume_Rank'] = volume.rank()

volume = volume.sort_values(by='Volume_Rank', ascending=False)

# %%
top_10 = volume.nlargest(n=10, columns='Volume')
ax = top_10['Volume'].plot(kind='bar')

# %%
clean_price_rank = clean_price.rank(axis=1)
