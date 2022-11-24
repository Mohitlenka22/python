import pandas as pd

df = pd.DataFrame()
print(df)

lst = ['java', 'python', 'c', 'cpp']
df1 = pd.DataFrame(lst)
print(df1)


data = {'Name': ['Tom', 'Joseph', 'ss'], 'Age':[20, 21, 19]}
df2 = pd.DataFrame(data)
print(df2)

data1 = [{'A':10, 'B':20}, {'x':100, 'y':200}]
df3 = pd.DataFrame(data1)
print(df3)