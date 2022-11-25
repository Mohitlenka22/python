import pandas as pd
import numpy as np

df = pd.DataFrame([['Mohit', 100, 10821345], ['KLN', 100, 72394056], ['Pavan', 100, 78789]], columns=['Name', 'Marks', 'Pop'])
print(df.nlargest(2, ['Marks', 'Pop']))
print(df.nsmallest(2, 'Marks'))