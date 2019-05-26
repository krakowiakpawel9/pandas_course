# -*- coding: utf-8 -*-
import pandas as pd


s = pd.Series(['#sport#good#time',
               '#workout#free#time',
               '#summer#holiday#hot'],
               name='hashtags')

# %%
split = s.str.split('#')

hashtag_1 = split.str.get(1)
hashtag_2 = split.str.get(2)
hashtag_3 = split.str.get(3)

# %%
df_concat_by_row = pd.concat([hashtag_1, hashtag_2, hashtag_3],
                             ignore_index=True)

string = df_concat_by_row.str.cat(sep=' ')

df_concat_by_row.str[0]
df_concat_by_row.str[:3]
# %%
df_concat_by_col = pd.concat([hashtag_1, hashtag_2, hashtag_3], axis=1)

# %%
split_2 = s.str.split('#', expand=True)

# %%
split_2 = s.str.split('#', expand=True, n=3)

# %%
s.str.replace('#', ' ')
s.str.replace('#', '_')
s.str.replace('#', '')

split_2.drop(0)
