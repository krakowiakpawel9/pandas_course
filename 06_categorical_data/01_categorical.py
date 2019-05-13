# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd


no = ['first_class', 'second_class', 'third_class', 'fourth_class']

min(no)
max(no)
sorted(no)

# %%
s = pd.Series(['cat_a', 'cat_b', 'cat_a'], dtype='category')

# %%
df = pd.DataFrame(np.random.rand(10, 2), columns=['a', 'b'])
df['c'] = df['b'].round(1).astype('category')

# %%

df = pd.DataFrame({'value': np.random.randint(0, 100, 50)})

labels = ['{} - {}'.format(i, i + 9) for i in range(0, 100, 10)]

df['group'] = pd.cut(df.value,
                     bins=range(0, 101, 10),right=False, labels=labels)

df.groupby('group').count()

# %%
raw_cat = pd.Categorical(['a', 'b', 'c', 'a'], categories=['b', 'c', 'd'],
                         ordered=False)

pd.Series(raw_cat)

# %%
