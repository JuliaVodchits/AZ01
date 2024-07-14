import pandas as pd

df = pd.read_csv('hh.csv')

df['Test'] = [new for new in range(0,len(df))]  # add a column with values
print(df)

df.drop('Test', axis=1, inplace=True)  # drop the column
print(df)

df.drop(len(df)-1, axis=0, inplace=True)  # drop a row
print(df)

df.to_csv('hh1.csv', index=False)  # save changes to new file
