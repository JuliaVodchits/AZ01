import pandas as pd

df = pd.read_csv('dz.csv')
print(df)

df.dropna(inplace=True)  # удалили строки с пустыми значениями
print(df)

group = df.groupby('City')['Salary'].mean() # вычислили среднее по группам
print(group)