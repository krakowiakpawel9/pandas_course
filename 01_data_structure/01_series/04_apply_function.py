# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

np.random.seed(10)

# Normal distribution, mean = 5, sigma = 10
s = pd.Series(10 * np.random.randn(20) + 5)

# %% applying built-in functions to Series
s.apply(abs)
s.apply(float.is_integer)
s.apply(int)

# %% applying custom functions to Series
s.apply(lambda x: 100 * x)
s.apply(lambda x: abs(x))
s_norm = s.apply(lambda x: (x - np.mean(s)) / np.std(s))
sigmoid = s_norm.apply(lambda x: 1 / (1 + np.exp(x)))


def custom_function(x):
    return 10 * x


s.apply(custom_function)


def simple_trans(x):
    return x + 100


series_trans = s.apply(simple_trans)


def more_complex(x):
    import math
    return math.sqrt(np.exp(x))


series_complex = s.apply(more_complex)


def sigmoid(x):
    return 1 / (1 + np.exp(x))


series_sigmoid = s.apply(sigmoid)
