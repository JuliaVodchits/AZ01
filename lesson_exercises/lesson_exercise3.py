import pandas as pd

df = pd.read_csv('World-happiness-report-2024.csv')
# print(df.head()) # 1st 5 rows
# print(df.tail()) # Last 5 rows
# print(df.info()) # info
# print(df.describe()) # min max etc.
# print(df[['Country name', 'Regional indicator']]) # some values from listed columns
# print(df.loc[56]) # all data from row 56
# print(df.loc[56, 'Country name']) # Country name from row 56
print(df[df['Healthy life expectancy'] > 0.7]) # filtered by column

