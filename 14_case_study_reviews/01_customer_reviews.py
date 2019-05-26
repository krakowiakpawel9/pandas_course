# -*- coding: utf-8 -*-
import pandas as pd


# %% import data
df = pd.read_csv('./data/reviews_clean.csv', index_col=0)

# %%
df['category'].value_counts().plot(kind='pie')

# %%
df['rating'].value_counts().plot('bar', legend=True, title='Frequency')

# %%
rat_count = df['rating'].value_counts().sort_index().plot('bar')

# %%
df['rating'].value_counts().sort_values()

# %% extract top 3 most rating products

top_3_no = df.groupby('name').count()['rating'].rename('count'). \
          sort_values(ascending=False).nlargest(3).plot(kind='pie')

# %% extract top 3 high rating product
top_3_rat = df.groupby('name').aggregate('mean').\
                               sort_values('rating', ascending=False).\
                               nlargest(3, columns='rating')

# %% extract bottom 3 product
bottom_3_rat = df.groupby('name').aggregate('mean')['rating'].\
                                  sort_values().nsmallest(3)
