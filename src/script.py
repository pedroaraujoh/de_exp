import pandas as pd

x = list()
x.append("test1")
x.append("test2")
print(f'x: {x}')

y = list()
y.append(1)
y.append(2)
print(f'y: {y}')

d = dict()
d = {'x': x, 'y': y}
print(f'd: {d}')

df = pd.DataFrame(data=d)
print('Pandas DataFrame')
print(df)