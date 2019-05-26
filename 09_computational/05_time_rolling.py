# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import seaborn as sns
sns.set()


dft = pd.DataFrame({'price': np.random.randn(97)},
                   index=pd.date_range('20190101 09:00:00', periods=97,
                                       freq='5min'))

fake_price = dft.cumsum()
fake_price_mean = fake_price.rolling(10).mean()
# %%
fake_price.plot()

# %%
stats = pd.concat([fake_price, fake_price_mean], axis=1)

# %%
fake_price_mean.plot()

# %%
fake_price
fake_price.rolling(window=10, min_periods=5).agg(np.mean)
