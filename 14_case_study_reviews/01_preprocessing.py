# -*- coding: utf-8 -*-
import pandas as pd


# %% import data
df = pd.read_csv('./data/Consumer_Reviews_Amazon.csv', index_col=0)

# %%
df.describe()

for col in df.columns:
    print(col)

# %% slicing

df = df[['name', 'primaryCategories', 'reviews.rating', 'reviews.text']]

# %% basic exploration

df.columns = ['name', 'category', 'rating', 'text']
df.info()
df.describe()

# %% export
df.to_csv('./data/reviews_clean.csv')
