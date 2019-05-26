# -*- coding: utf-8 -*-
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# %%
tit = sns.load_dataset('titanic')

# %%
tit.groupby('sex').size().plot(kind='bar', alpha=0.5)
tit.groupby(['sex', 'survived']).size()

# %%
tit.groupby('sex').mean()['survived']
tit.groupby(['sex', 'class']).mean()['survived'].unstack().\
    plot(kind='bar', subplots=True, layout=(1, 3), sharey=True)

tit.pivot_table('survived', index='sex', columns='class')
tit.pivot_table('survived', index='sex', columns='class')

# %%
tit['age_bin'] = pd.cut(tit['age'], bins=[0, 18, 80])
tit.pivot_table('survived', index='age_bin', columns='class', aggfunc='count')


# %%
fig, ax = plt.subplots(1, 2, sharey=True)
tit.groupby(['sex', 'survived']).size()['male'].plot(ax=ax[0], kind='bar')
tit.groupby(['sex', 'survived']).size()['female'].plot(ax=ax[1], kind='bar')
ax[0].legend('male')
ax[1].legend('female')

# %%
r = pd.pivot_table(tit, values='age', index='survived', columns='sex',
                   aggfunc='count')
r.plot(subplots=True, kind='bar', sharey=True, layout=(1, 2))

# %%
r = pd.pivot_table(tit, values='age', index='survived', columns='who',
                   aggfunc='count')
r.plot(subplots=True, kind='bar', sharey=True, layout=(1, 3), cmap='viridis')

# %%
r = pd.pivot_table(tit, values='age', index='survived', columns=['sex', 'who'],
                   aggfunc='count')
r.unstack(level=0)

# %%
age = tit['age']
age_bin = pd.cut(age, bins=[0, 18, 80])
age_qbin = pd.qcut(age, 4)
tit['qbin'] = pd.qcut(age, 4)
tit.groupby('qbin').size()

# %%
tit.pivot_table(index='sex', columns='class',
                aggfunc={'survived': sum, 'fare': 'mean'})
