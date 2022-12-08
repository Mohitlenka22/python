import pandas as pd
import matplotlib.pyplot as plt

# df = pd.DataFrame({'Name' : ['Mohit', 'KLN', 'Pavan', 'Guna sekhar'], 'Marks' : [91, 100, 97, 94]})

'''Bar plots
df.plot.bar(x='Name', y='Marks', rot=1, color='red')
df.plot.bar(subplots=True, rot=1, color='red')
plt.show()
'''

'''histogram plot
df = pd.DataFrame({'Name' : ['Mohit', 'KLN', 'Pavan', 'Guna sekhar'], 'Marks' : [91, 100, 97, 94], 'Age':[19, 20, 19, 18]})

df.plot.hist(alpha = 0.7)
plt.show()
'''

'''scatter
df1 = pd.DataFrame({'x' : [1, 3, 5, 7, 8], 'y' : [0, 6, 7, 8, 10]})
df2 = pd.DataFrame({'x' : [1, 3, 4, 56], 'y':[1, 5, 7, 8]})
ax = df2.plot.scatter(x = 'x', y = 'y', color = 'yellow')
df1.plot.scatter(x = 'x', y = 'y', color = 'red', ax = ax)
plt.show()
'''

'''line plots'''
year = [2001, 2003, 2010, 2013, 2020]
unemployment_rate = [22, 10, 30, 33, 39]

plt.plot(year, unemployment_rate)
plt.xlabel('year')
plt.ylabel('unemp%')
plt.show()


