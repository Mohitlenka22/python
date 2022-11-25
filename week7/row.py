import pandas as pd
import numpy as np

df = pd.DataFrame(np.array([['Mohit', 100], ['KLN', 100], ['Pavan', 100]]), columns=['Name', 'Marks'])
print(df)

#row selection
print(df.loc[0:1])

#row addition
df2 = pd.DataFrame(np.array([['Guna Sekhar' ,100]]), columns = ['Name', 'Marks'])
print(pd.concatenate(df, df2))

