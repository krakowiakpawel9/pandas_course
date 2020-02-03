# -*- coding: utf-8 -*-

"""
@author: krakowiakpawel9@gmail.com
@site: e-smartdata.org
"""

import numpy as np
import pandas as pd


df_1 = pd.DataFrame(np.random.randint(0, 10, 100))

df_1_unique = df_1.drop_duplicates()