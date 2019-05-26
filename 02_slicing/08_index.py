# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

# %%
np.random.seed(0)
idx = pd.Index(['5364', '3445', '3343', '5732'])

df = pd.DataFrame(np.random.randn(4, 5),
                  columns=list('abcde'),
                  index=idx)
