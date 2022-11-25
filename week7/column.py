import pandas as pd
import numpy as np

# d = {'Name':['Mohit', 'KLN', 'Guna Sekhar'], "Marks":[100, 99, 98], 'Age':[19, 19, 19]}
df = pd.DataFrame(np.array([['Mohit', 100, 19], ['KLN', 99, 19], [
                  'Guna Sekhar', 98, 19]]), columns=['Name', 'Marks', 'Age'])
print(df)

# selection
print(df['Name'])
print(df['Marks'])
print(df['Age'])
print(df.columns)

# additon
df['section'] = [2, 1, 2]
print(df)

# deletion
del df['Age'], df['section']
print(df)

df.drop(['Name', 'Marks'], axis=1, inplace=True)
print(df)
