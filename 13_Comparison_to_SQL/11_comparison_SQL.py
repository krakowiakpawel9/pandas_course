# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd


url = ('https://archive.ics.uci.edu/ml/machine-learning-databases/00352/'
       'Online%20Retail.xlsx')

retail = pd.read_excel(url)

# %%
retail.info()
desc = retail.describe()

cols = [col for col in retail.columns]

print(retail.head())

# %% preprocessing
# drop rows with null
retail = retail[retail['CustomerID'].notnull()]

# convert type to string
retail['CustomerID'] = retail['CustomerID'].apply(lambda x: str(int(x)))

# exclude Quantity less than zero
retail = retail[retail['Quantity'] >= 0]

# %%
"""
SELECT *
FROM retial;
"""
query = retail

# %%
"""
SELECT Quantity, UnitPrice, CustomerID
FROM retial;
"""
query = retail[['Quantity', 'UnitPrice', 'CustomerID']]

# %%
"""
SELECT Quantity, UnitPrice, CustomerID
FROM retial
LIMIT 10;
"""

query = retail[['Quantity', 'UnitPrice', 'CustomerID']][:10]
query_ = retail[['Quantity', 'UnitPrice', 'CustomerID']].head(10)

# %%
"""
SELECT *
FROM retial
WHERE CustomerID='17850';
"""

query = retail[retail['CustomerID'] == '17850']
query_ = retail.query('CustomerID == "17850"')

# %% and
"""
SELECT *
FROM retial
WHERE CustomerID='17850' and UnitPrice > 5;
"""

query = retail[(retail['CustomerID'] == '17850') & (retail['UnitPrice'] > 5)]
query_ = retail.query('CustomerID == "17850" and UnitPrice > 5')

# %% or
"""
SELECT *
FROM retial
WHERE CustomerID='17850' or Country='France';
"""

query = retail[(retail['CustomerID'] == '17850') | (retail['Country']
               == 'France')]
query_ = retail.query('CustomerID == "17850" or Country == "France"')

# %% isnull
"""
SELECT *
FROM retail
WHERE InvoiceNo is null;
"""
retail[retail['InvoiceNo'].isnull()]
retail[retail['StockCode'].isnull()]

# %% is not null
"""
SELECT *
FROM retail
WHERE InvoiceNo is not null;
"""
retail[retail['InvoiceNo'].notnull()]

# %% group by
"""
SELECT CustomerID, count(*)
FROM retial
GROUP BY CustomerID;
"""
cust_id = retail.groupby('CustomerID').size()
countries = retail.groupby('Country').size()

# %% compute new cols
retail['Revenue'] = retail['Quantity'] * retail['UnitPrice']

# %% group by
"""
SELECT CustomerID, avg(Revenue), count(*)
FROM retial
GROUP BY CustomerID;
"""
revenue_by_cust_id = retail.groupby('CustomerID').\
                            aggregate({'Revenue': np.mean,
                                       'CustomerID': np.size}).\
                            rename(columns={'Revenue': 'AverageRevenue',
                                            'CustomerID': 'Count CustomerID'})

# %%
retail['InvoiceDateDay'] = retail['InvoiceDate'].dt.day

# %%
query = retail.groupby('InvoiceDateDay').aggregate({'Revenue': np.sum})

query.plot(kind='bar', color='black', alpha=0.5, title='Sales by day')

# %%
day_9 = retail[(retail['InvoiceDate'] > '2010-12-09') &
               (retail['InvoiceDate'] < '2010-12-10')]
day_9['Hour'] = day_9['InvoiceDate'].dt.hour

query = day_9.groupby('Hour').aggregate({'Revenue': np.sum})

query.plot(kind='bar', color='blue', alpha=0.5, title='Sales by hour')

# %% top n rows
"""
SELECT * FROM retail
ORDER BY Quantity DESC
LIMIT 5;
"""
query = retail.nlargest(5, columns='Quantity')

# %% bottom n rows
"""
SELECT * FROM retail
ORDER BY Quantity
LIMIT 10;
"""
query = retail.nsmallest(5, columns='Quantity')