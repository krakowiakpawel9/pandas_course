# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd


# %%
df = pd.DataFrame(np.random.rand(1000))

# %%
df.hist()

# %%
df.plot.hist()

# %%
df.plot(kind='hist')

# %%
df.plot.hist(bins=20, cmap='viridis')

# %%
df = pd.DataFrame(np.random.randn(10000))
df.plot.hist(bins=40, color='red', alpha=0.5)

# %%
df = pd.DataFrame({'mu_0_sigma_1': np.random.randn(10000),
                   'mu_1_sigma_2': 2 * np.random.randn(10000) + 1,
                   'mu_8_sigma_3': 3 * np.random.randn(10000) + 8})
df.plot.hist(bins=40, cmap='viridis', alpha=0.5,
             title='Different Normal Distribution')

# %% cumulative plot
df['mu_8_sigma_3'].plot.hist(cumulative=True, bins=1000, color='green',
                             alpha=0.5)

# %%
df.hist(sharex=True, sharey=True)
