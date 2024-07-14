import pandas as pd

data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'Anna'],
        'Age': [20, 30, 40, 23],
        'City': ['San Francisco', 'New York', 'Los Angeles', 'Moscow']
    }
df = pd.DataFrame(data)
print(df)