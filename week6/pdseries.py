import numpy as np
import pandas as pd


# # list
# l = [1, 3, 5, 7]
# ser = pd.Series(l)
# print(ser)
# print(ser[:2])
# # np array
# arr = np.array(l)
# ser = pd.Series(arr, index=['a', 'b', 'c', 'd'])
# print(ser)

# dataframe
df = pd.read_csv('data.csv')
ser = pd.Series(df['Name'])
head_data = ser.head(5)
print(f'head_data: {head_data}')
loc = head_data.loc[0:4]
print(f'loc: {loc}')
tail_data = ser.tail(3)
print(f'tail_data: {tail_data}')
iloc = tail_data.iloc[2]
print(f'iloc {iloc}')
desc = head_data.describe()
print(f'desc: {desc}')

# #add, sub
# d1 = pd.Series([5, 4, 7, 9], index=['a', 'b', 'c', 'd'])
# d2 = pd.Series([8, 9, 1, 4], index=['a', 'b', 'd', 'e'])
# ans1 = d1.add(d2, fill_value=0)
# print(ans1)
# ans2 = d1.sub(d2, fill_value=0)
# print(ans2)
