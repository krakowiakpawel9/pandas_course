# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd


# %%
df = pd.DataFrame(np.random.randn(100, 4),
                  columns=list('ABCD'))

s = pd.Series(np.random.randint(0, 2, 100), name='Flag')

df = pd.merge(df, s, how='inner', left_index=True, right_index=True)
# %%
df = df.drop('Flag', axis=1)
df = df.cumsum()
bar_data = df.iloc[-1].apply(abs)
bar_data.plot(kind='bar', title='Random generated data', cmap='viridis')

# %% multiple bar plot vertical
df_bar = pd.DataFrame(np.random.rand(10, 4),
                      columns=list('ABCD'))
df_bar.plot.bar(cmap='viridis', title='Multiple bar plot', alpha=0.7)

# df_bar.plot(kind='bar', cmap='viridis', title='Multiple bar plot')

# %% multiple bar plot horizontal
df_bar.plot.barh(cmap='viridis', title='Horizontal bar plot')

# %% stacked bar plot vertical
df_bar.plot.bar(stacked=True, cmap='viridis', alpha=0.5)

# %%  stacked bar plot horizontal
df_bar.plot.barh(stacked=True, cmap='viridis', alpha=0.5)
