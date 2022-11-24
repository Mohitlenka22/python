import pandas as pd

d = {'a' : 1, 'b' : 2, 'c' : 3}
ser = pd.Series(d)
# ser = pd.Series(d, index = ['a', 'b', 'c'])
print(ser)