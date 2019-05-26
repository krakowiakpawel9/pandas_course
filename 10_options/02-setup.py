# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import seaborn as sns
sns.set()

# %%
pd.set_option('display.max_rows', 999)
pd.set_option('precision', 3)

pd.describe_option('precision')
pd.get_option('expand_frame_repr')
pd.set_option('large_repr', 'info')
# %%
df = pd.DataFrame(np.random.rand(100, 4),
                  columns=['a', 'b', 'cust_tab_dev_prod_dict_flg', 'd'])
print(df)
# %%
df.info()
df.memory_usage()
