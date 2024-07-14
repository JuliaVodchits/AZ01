import pandas as pd

df = pd.read_csv('animal.csv')
print(df)

# df.fillna(0, inplace=True) # replace NaN
# df.dropna(inplace=True)  # drops rows with NaN

# group = df.groupby('Пища')['Средняя продолжительность жизни'].mean() #  среднее значение поля внутри группировки
# print(group)