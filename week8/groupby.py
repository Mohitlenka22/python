import pandas as pd

df = pd.DataFrame({'Name':['Mohit', 'KLN', 'Guna Sekhar'], 'Marks':[100, 99, 98]})

# print(df.groupby(['Name', 'Marks']).groups)
grouped = df.groupby('Name')
for name, group in grouped:
    print(name, group)