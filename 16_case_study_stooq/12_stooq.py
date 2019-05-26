# -*- coding: utf-8 -*-
from pandas_datareader.stooq import StooqDailyReader
import pandas as pd


companies = {'MSFT.US': 'Microsoft Corporation', 'AAPL.US': 'Apple Inc.',
             'GOOGLE.US': 'Alphabet Inc.', 'FB.US': 'Facebook', 'CSCO.US':
             'Cisco Systems', 'INTC.US': 'Intel Corporation', 'ORCL.US':
             'Oracle Corporation', 'SAP.US': 'SAP SE', 'CRM.US':
             'Salesforce.com Inc.', 'IBM.US': 'IBM Corporation',
             'NVDA.US': 'Nividia Corporation', 'VMW.US': 'Vmware, Inc.',
             'UBER.US': 'Uber Technologies', 'RHT.US': 'Red Hat, Inc.',
             'TEAM.US': 'Altassian Corporation', 'TWTR.US': 'Twitter, Inc.',
             }

# %% extract list of tickers
tickers = sorted([ticker for ticker in companies.keys()])

# %%


def download_data(ticker):
    df = StooqDailyReader(symbols=(ticker)).read()
    cols = {col: col + '_' + ticker for col in df.columns}
    df = df.rename(columns=cols)
    return df


def create_big_df(n=2):
    frames = []
    for ticker in tickers[:n]:
        df = download_data(ticker)
        frames.append(df)

    return pd.concat(frames, axis=1, join='outer')


# %%
big_df = create_big_df(3)

close_col = [col for col in big_df.columns if col.startswith('Close')]
close_df = big_df[close_col]
c = close_df.corr()
