# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd


left = pd.DataFrame(np.random.rand(10, 3),
                    index=pd.date_range('2019-01-01', periods=10),
                    columns=list('abc'))

right = pd.DataFrame(np.random.rand(10, 3),
                     index=pd.date_range('2019-01-04', periods=10),
                     columns=list('def'))

# %% left
left_join = left.join(right, how='left')

# %% right
right_join = left.join(right, how='right')

# %% inner
inner_join = left.join(right, how='inner')
# %% outer
outer_join = left.join(right, how='outer')
