# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import seaborn as sns
sns.set()


# setting max rows to display
pd.options.display.max_rows = 10

# %%
df = pd.DataFrame(np.random.randn(100, 3))

# %% get value of option
pd.get_option('display.max_rows')

# %% set value of option
pd.set_option('display.max_rows', 30)
pd.get_option('display.max_rows')

pd.reset_option('display.max_rows')
pd.get_option('display.max_rows')

pd.describe_option('display.max_rows')
pd.describe_option('mode.sim_interactive')