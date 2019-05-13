# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np


# %% read data from clipboard
df_raw = pd.read_clipboard()
df = df_raw.copy()

# get list of columns
columns = [col for col in df.columns]

# %% preprocessing
df = df.drop(['Czas', '1r 3m'], axis=1)
