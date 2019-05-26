# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('./data/googleplaystore.csv')

# %%
columns = [col for col in df.columns]
df.info()

df = df.drop(10472)
df = df.reset_index()

df['Reviews'] = pd.to_numeric(df['Reviews'])
df.info()

# %% categories frequency
category_freq = df.groupby('Category').agg('count')['App'].rename('Count')
category_freq.plot(kind='bar', color='purple', alpha=0.5,
                   title='Categories Frequency')

# %% type frequnecy
type_freq = df.groupby('Type').agg('count')['App'].rename('Count')
plt.figure()
type_freq.plot(kind='pie', cmap='viridis', fontsize=14,
               title='Reviews based on type')

# %%
agg = df[['Genres', 'Rating', 'Type']].groupby(['Genres', 'Type']).
                                       agg({'Rating':['count', 'mean']})
agg.columns = ['_'.join(x) for x in agg.columns.ravel()]
agg = agg.sort_values(by='Rating_count', ascending=False)
agg = agg[agg['Rating_count'] > 100]
agg.plot(kind='bar', subplots=True, cmap='viridis')

# %%
agg_top_5 = agg.nlargest(n=5, columns='Rating_count')
agg_top_5.plot(kind='pie', subplots=True, cmap='viridis')

