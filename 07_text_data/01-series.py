# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd


s = pd.Series(['Apple', '   Microsoft', np.nan, '  Google  ', 'Anazon'])

# %%
s = s.str.strip()

# %%
lower = s.str.lower()

# %%
upper = s.str.upper()

# %%
length = s.str.len()

# %% case
df = pd.DataFrame(np.random.rand(10, 2),
                  columns=['          ID value ', '  Price'])

# %%
df.columns = df.columns.str.strip()

# %%
df.columns = df.columns.str.lower()

# %%
df.columns = df.columns.str.replace(' ', '_')
