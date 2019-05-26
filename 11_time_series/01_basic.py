# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import pytz

"""
Symbol  |  Meaning
------------------
D - Calendar Day
B - Business Day
W - Weekly
M - Month End
MS - Month Start
BM - Business Month End
BMS - Business Month Start
Q - Quarter End
QS - Quarter Start
BQ - Business Quarter End
BQS - Business Quarter Start
A - Year End
AS - Year Start
BA - Business Year End
BAS - Business Year Start
H - Hours
BH - Business Hours
T - Minutes
S - Seconds
L - Miliseconds
U - Microseconds
N - Nanoseconds

offset:
-------
QS-FEB
A-MAR
W-MON
"""

# %% creating DatetimeIndex object
# default frequency: day
rng = pd.date_range('2019-01-01', periods=100)

rng = pd.date_range('2019-01-01', periods=100, freq='S')
rng = pd.date_range('2019-01-01', periods=100, freq='M')
rng = pd.date_range('2019-01-01', periods=100, freq='MS')
rng = pd.date_range('2019-01-01', periods=100, freq='3M')
rng = pd.date_range('2019-01-01', periods=100, freq='H')
rng = pd.date_range('2019-01-01', periods=100, freq='6H')
rng = pd.date_range('2019-01-01', periods=100, freq='B')
rng = pd.date_range('2019-01-01', periods=100, freq='Q')
rng = pd.date_range('2019-01-01', periods=100, freq='QS')
rng = pd.date_range('2019-01-01', periods=100, freq='MIN')
rng = pd.date_range('2019-01-01', periods=100, freq='T')
rng = pd.date_range('2019-01-01', periods=100, freq='W')
rng = pd.date_range('2019-01-01', periods=100, freq='A')
rng = pd.date_range('2019-01-01', periods=100, freq='QS-FEB')
rng = pd.date_range('2019-01-01', periods=100, freq='W-MON')
rng = pd.date_range('2019-01-01', periods=100, freq='2H30T')


# %%
time_zones = list(pytz.all_timezones)
europe = [tz for tz in time_zones if tz.startswith('Europe')]

# %%
rng = pd.date_range('2019-01-01', periods=100, freq='MS', tz='Europe/Warsaw')

rng = pd.date_range('2019-01-01', periods=200, freq='D', tz='Europe/Warsaw')

rng.tz_convert(tz='US/Central')

# %%
rng = pd.date_range('2019-01-01', periods=100, freq='MIN', tz='Europe/Warsaw')
ts = pd.Series(np.random.rand(100), index=rng)
ts_period = ts.to_period()

ts.plot()
ts_period.plot()

ts_sample = ts.resample('5MIN').sum()
ts_sample = ts.resample('15MIN').sum()
ts_sample = ts.resample('15MIN').asfreq()
ts_sample.plot()

# %%
rng = pd.date_range('2019-01-01', periods=10, freq='AS', tz='Europe/Warsaw')
ts = pd.Series(np.random.randn(10), index=rng)
ts.resample('2A').sum()

ts.to_period()

# %%
rng = pd.date_range('2019-01-01', periods=100, freq='5MIN', tz='Europe/Warsaw')
ts = pd.Series(rng, name='Upload time')
ts.dt.hour
ts.dt.minute

# %%
df = pd.DataFrame({'num_val': pd.Series(np.random.rand(100)),
                   'time_val': pd.Series(rng)})

df['time_val_min'] = df['time_val'].dt.minute

df['time_val_hour'] = df['time_val'].dt.hour

# %%
mask = df['time_val'].dt.hour == 6
df[mask]

# %%
rng = pd.date_range('2019-01-01', periods=100, freq='D', tz='Europe/Warsaw')
df = pd.DataFrame({'num_val': pd.Series(np.random.rand(100)),
                   'time_val': pd.Series(rng)})

df['time_val_day_of_week'] = df['time_val'].dt.dayofweek
df['time_val_day_of_year'] = df['time_val'].dt.dayofyear
df['time_val_week_of_day'] = df['time_val'].dt.weekofyear