import pandas as pd

df = pd.read_excel('BRICS Economic Data.xlsx')
print(df.head())
print(df.info())
print(df.describe())