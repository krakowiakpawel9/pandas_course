# -*- coding: utf-8 -*-
import pandas as pd


df = pd.read_csv('./data/ten_d.csv', index_col=0)
df.columns = ['Open', 'High', 'Low', 'Close', 'Volume']

# %% pct_change()
df['Daily_Change'] = df['Close'].pct_change()

# %%
df['Daily_Change_Manually'] = df['Close'] / df['Close'].shift() - 1

# %%
df['5_Days_Change'] = df['Close'].pct_change(periods=5)

# %%
df['Close_To_Open'] = df[['Open', 'Close']].pct_change(axis=1).\
                                            drop('Open', axis=1)

# %%
clean_price = df[['Open', 'High', 'Low', 'Close']]

daily_change = clean_price.pct_change()

max_p = daily_change.max()
min_p = daily_change.min()
ax = max_p.plot.bar(cmap='viridis', figsize=(10, 7), fontsize=13)
ax.set_title('Max daily changes')
ax.set_xlabel('Type of price', fontsize=13)

totals = []
for i in ax.patches:
    totals.append(i.get_height())


for i in ax.patches:
    ax.text(i.get_x() + 0.13, i.get_height() + 0.005,
            str(round(100 * i.get_height(), 2)) + '%')
