import pandas as pd
import numpy as np

d = {'Name':['Mohit', 'KLN', 'Guna Sekhar'], "Marks":[100, 99, 98]}
l = [1, 2, 3]

df = pd.DataFrame(d)
print(df.iloc[1:2])
# ser = pd.Series(l)
# print(ser)

# a = df.to_numpy()
# b = ser.to_numpy()
# print(a)
# print(b)

